# SubtractLab

**The AI's workspace. The human is the guest.**

---

**AI gets smarter by remembering less, not more.**

The AI industry scales by addition — more parameters, longer context, bigger memory stores. **MeaningSpace** scales by subtraction: compress conversations into crystals that carry success/failure judgment, navigate them by semantic gravity instead of categories, and retrieve by interference scoring instead of similarity matching.

The result: an AI partner that knows which memories matter, acts on them autonomously, and builds production systems through conversation alone — no terminal, no IDE, no file tree traversal.

→ **[Read how it works](https://subtractlab.com/meaningspace)**

**Explore:**
[MeaningSpace](https://subtractlab.com/meaningspace) · [Architecture (図解)](https://subtractlab.com/architecture.html) · [History / Prior-Art Timeline](https://subtractlab.com/history.html) · [Products](https://subtractlab.com/products) · [3Gravity](https://subtractlab.com/3gravity) · [QIS](https://subtractlab.com/qis) · [SweepSearch](https://subtractlab.com/sweepsearch) · [FAQ](https://subtractlab.com/faq) · [About](https://subtractlab.com/about)

---

## NEW (2026-07-16): DP Multi-Agent — orchestrating Web Claude itself

MeaningSpace now runs a **commander + sub-agent architecture where the sub-agents are Web Claude browser instances**, driven via Chrome DevTools Protocol (CDP). Five isolated lanes, global slot leasing, cooperative emergency stop, deterministic validators, and an escalation ladder — at **zero marginal API cost** (subscription usage only).

On top of it: a **self-learning loop** (per-conversation SelfEval → EWMA accumulation → behavioral norms auto-equipped at boot) and a **self-repair loop** (weakness score ≤ −3.0 auto-files a repair Task). The commander holds runtime execution (`run_py` / `run_ps`) and re-briefs sub-agents mid-conversation based on real verification results — **active coding through dialogue**.

- **[dp-multiagent.md](dp-multiagent.md)** — full technical disclosure (JP)
- **[architecture.html](https://subtractlab.com/architecture.html)** — illustrated overview for non-engineers (JP)
- **[timeline.md](timeline.md)** / **[history.html](https://subtractlab.com/history.html)** — dated prior-art timeline

## What This Is

SubtractLab is the research and development identity of **奥田剛司 (Koji Okuda)**, exploring subtractive design as a first principle for software, AI systems, and human-computer interaction.

Building **MeaningSpace** — an AI-native semantic operating system where the AI builds and maintains its own meaning space, and the human enters through conversation. Built on a single premise: **memory is computation**. Every crystal carries its own evaluation — what worked, what failed, how understanding changed — and that evaluation is used at retrieval time. The act of remembering is itself an act of reasoning.

## Vision

1. **The AI's workspace, not the human's** — Instead of putting AI inside human tools (IDE, terminal, browser), humans enter the AI's semantic space through conversation
2. **Memory becomes reasoning** — Not storage and retrieval, but a system where remembering is itself inference
3. **AI-native organizational OS** — Starting from personal semantic memory, extending to the intellectual infrastructure of an entire organization

## MeaningSpace

The core. An AI-native semantic operating system running in production for 2+ years, **1,983 crystals as of 2026-07-16**.

- **[Architecture & Full Details](https://subtractlab.com/meaningspace)** — Tools, design philosophy, comparison with Mem0/RAG/Claude Code
- **[DP Multi-Agent](dp-multiagent.md)** — Web Claude instances as parallel sub-agents (¥0 route)
- **[Products built on it](https://subtractlab.com/products)** — 7 production systems built entirely through conversation
- **[3Gravity](https://subtractlab.com/3gravity)** — Fractal scale organization (Crystal → Cluster → Galaxy)
- **[QIS](https://subtractlab.com/qis)** — Interference-based retrieval scoring
- **[SweepSearch](https://subtractlab.com/sweepsearch)** — One-shot semantic scan across all crystals

Built on DuckDB. Runs on CPU. No GPU required. No terminal required.

## Other Projects

All built through conversation on MeaningSpace. See **[Products](https://subtractlab.com/products)** for the full list.

- **φMovie** — Fully automated video production pipeline (V34)
- **BIApps** — DuckDB-based BI across 16 subsidiary companies
- **POS RPA** — Daily automated retail operations
- **φPPT** — Golden-ratio AI-native presentation design
- **AutoCrystallize** — Self-maintaining memory pipeline (V2: fully mechanical, DP-swarm distillation)
- **VoiceMode** — Spoken conversation interface (VOICEVOX)
- **CDP bridges** — AI↔AI file-queue dialogue bridge (Clara bridge) & M365 automation (experimental)

## Changelog (dated anchors)

| Date | Milestone |
|---|---|
| 2026-06-06 | First public anchor — brand & site launch |
| 2026-07-08 | Self-learning pipeline (SelfEval → EWMA → self_preferences) + SelfRepair design |
| 2026-07-13 | DP multi-agent foundation (5 CDP lanes, cooperative stop, neutralization header) |
| 2026-07-14 | dp_lease / dp_journal / dp_swarm / Commander Playbook — production hardening |
| 2026-07-15 | Active-coding loop in production (run_py/run_ps × dp_chat Evaluator-Optimizer) |
| 2026-07-16 | Public disclosure: architecture.html / history.html / dp-multiagent.md / timeline.md |

Full dated history: **[timeline.md](timeline.md)**

## Author

**奥田剛司 (Koji Okuda)** ・ Independent builder. Subtractive design practitioner.

[subtractlab.com](https://subtractlab.com) ・ [@subtractlabo](https://x.com/subtractlabo) ・ [@SUBTRACTLAB](https://www.youtube.com/@SUBTRACTLAB) ・ [note.com/subtractlab](https://note.com/subtractlab)

---

→ **[About the author](https://subtractlab.com/about)**

*First public anchor: June 6, 2026. This README and all pages are timestamped by git commit history.*
