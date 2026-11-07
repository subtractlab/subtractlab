# DP Multi-Agent — a ¥0 multi-agent foundation that orchestrates web Claude

**First published: 2026-07-16 (JST) / SubtractLab**
Related: [architecture.html](https://subtractlab.com/architecture.html) · [timeline.md](timeline.md) · [meaningspace.md](meaningspace.md)

> DP = **Debug Port**. The claude.ai chat page is driven mechanically over the Chrome DevTools Protocol (CDP), and a set of web Claude instances runs as parallel sub-agents. No pay-per-use API is involved; it runs entirely on the web allowance of a flat-rate subscription (¥0 extra cost). This is the public version of primary findings fixed by measurement between 2026-07-13 and 07-15.

## 1. The physical model

- **One lane = one Chrome = one profile = one CDP port = one dedicated thread.** With zero shared state, adding lanes does not break the structure.
- Five lanes: DP1 to DP5. The ledger is `lanes.json` (the source of truth for window positions, default model and max_concurrent). UI dependencies are isolated in `selectors.json`.
- Every entry point (bulk swarm / dialogue / worker / pipeline) goes through a shared lane client, which places the windows and titles each lane automatically at start.
- A new lane is a copy of an existing profile (the logged-in session comes with it). Copy only while Chrome is stopped.

## 2. The physics of concurrency — measured values

| Fact | Detail |
|---|---|
| Concurrency limit | Not published. Measured at **two per account**. The commander's own replies (Claude on the desktop) take one of them |
| Control | `dp_lease.py` — a lock across processes using ticket files. Stale recovery when the process dies or after 15 minutes. Wired into every entry point (made permanent 2026-07-14) |
| Staggered starts | Several submissions in the same millisecond make UI actions collide and freeze a lane (measured: stuck at msgs=0 for 120 s) → stagger of 2.5 s. The cost is a few seconds |
| Over the allowance | Putting work back on the queue makes it look "empty for a moment", every worker leaves and the groups disappear (measured: 5 of 11 groups lost). **Wait in place and resend** instead (5 tries → marked failed) |

## 3. Zombie responses and the order of stopping (the most important safety finding)

Generation on claude.ai runs **on the server**. Killing the local process or closing the browser does not stop it, and it keeps holding a concurrency slot (a zombie response).

**Always stop in this order:**
1. Abort flag (cooperative stop — workers check the flag at group boundaries and leave)
2. Press "Stop response" in each lane's UI, mechanically
3. Kill the process

The reverse order leaves the slots held. Measured: from three generations in progress, one emergency stop **stopped everything in 3.6 s**. Every swarm also fires a stop in a pre-flight step to clear leftovers before it starts. **Threads cannot be killed. A cooperative stop is the only correct answer.**

## 4. State detection — no more decisions from UI strings

At first, rate-limit warnings were detected by matching text across the whole page. The detector then **read the same warning inside past logs included in the prompt and refused its own work** (self-reference contamination). Countermeasures (2026-07-14):

- Decisions based only on DOM attributes — looking at the **outside** of message containers only (user-message, streaming attributes, article roles)
- Leftover toasts removed from the DOM just before sending
- A standing regression test that feeds prompts containing UI warning text

## 5. Persona contamination and the neutralizing header

All DP lanes share one account, so the user's custom settings (persona and output-format instructions) also apply to the sub-agents. **Incognito chats do not turn them off** (measured: only memory is turned off). The countermeasure is a **neutralizing header** at the top of the contract prompt — an explicit statement that user settings do not apply to this task. Measured to return the lanes to plain assistant replies (2026-07-13).

## 6. How files are handled — the one who touches and the one who decides

Claude in a browser has no file system. So:

1. **Hydrate** — the commander puts the target source into the prompt
2. **Generate** — DP returns only a body or a diff (anchor-replace / the `===NEWFILE path=...===` convention)
3. **Apply and verify** — the commander applies it and checks it

**DP is never given delete permission.** Hydration puts the body of someone else's file into the prompt, so a line inside it saying "delete this file" could pass as an injection. Deleting stays with the commander alone, behind its own gates.

## 7. Ways to run — Chain / Swarm / Loop

| Form | Structure | Use |
|---|---|---|
| Chain | In sequence (each stage's output feeds the next) | Scout → implement → verify |
| Swarm | Parallel fan-out (two effective lanes) | Bulk conversion, extraction and single-file generation |
| Loop | DP generation × local deterministic checks, in rounds | Code fixes, pinning down a spec |

**The swarm production base, `dp_swarm.py` (completed 2026-07-14):** tasks.json (objective + validator) → submit all → collect results.json / journal.jsonl. Validators: py_compile / json / regex / any command / nonempty. The escalation ladder: **Haiku first → deterministic check → on failure retry the same model twice → escalate to a stronger model (thinking on) twice → still failing: failed**. Benchmark 4/4 PASS, 9–15 s per item, ¥0 extra cost.

Response cleaning made permanent: (1) remove lines read out by the UI, (2) strip output-convention markers, (3) code must be fenced (the chat page does not preserve indentation outside fences).

**Loop = active coding:** the commander runs its own checks and **sends fixes back to the dialogue lane (dp_chat) on the strength of checks run mid-conversation** — an evaluator-optimizer. First real use was 2026-07-15: DP implemented the F6 flow hook v2 (a mechanism that detects the moment an AI answers without consulting its memory) through this loop.

## 8. Observability and the commander

- `dp_journal.py` — journal.jsonl and summary.json per run. Ownership by group; a run ends when every group reaches a terminal state.
- `COMMANDER_PLAYBOOK.md` — the commander's decision table: task type → preset, first responses to failure patterns, and how to read the journal.
- The commander never receives a sub-agent's full reply (only extraction paths and a short summary). **Separating eyes from hands** keeps context use down.

## 9. Cost structure

| Route | Cost |
|---|---|
| Pay-per-use API (old route) | Metered (measured on this system: about ¥18 per run) — sealed; starts only with the human's approval |
| **DP route** | **¥0 extra** (consumes only the flat-rate web allowance, shared across the account; the number of lanes affects how fast it is used) |

DP is not a loophole in billing; it is **a way of designing parallelism within a flat-rate allowance**.

## 10. What sits on top

The DP lanes are the foundation. On top of them:

- **AutoCrystallize V2** — conversation logs → split by meaning (cosine valleys) → distilled by a DP swarm → merged and inspected → crystals. Started with one command; completion detected asynchronously by a done marker.
- **Self-learning** — a SelfEval crystal for every conversation, accumulated with decay (EWMA) and worn at boot as behavioral norms (self_preferences) (implemented 2026-07-08, v8 live).
- **Self-repair** — a repair task is filed automatically when a weakness score drops to −3.0 or below. One word from the human bundles them for a DP swarm to clear.

---
*Every fact here comes from MeaningSpace crystals (timestamped development records) on the developer's local machine. For the list of dates, see [timeline.md](timeline.md).*
