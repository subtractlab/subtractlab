# MeaningSpace / DP Multi-Agent — Prior-Art Timeline

**First published: 2026-07-16 (JST) · Updated 2026-11-07 · SubtractLab (one builder + AI)**

The confirmed date of each mechanism's design, implementation and proof. Source: crystals inside MeaningSpace (timestamped, structured development records). The git history of this repository serves as a third-party-verifiable timestamp. Illustrated version: [history.html](https://subtractlab.com/history.html)

## Era 1 — Talking with AI, automating work
| Date | Event |
|---|---|
| 2023-02 | First conversations with AI (ChatGPT) — The first conversation is dated 2023-02-07. The 1,567 ChatGPT conversations from this period were later imported into MeaningSpace and can still be retrieved. |
| 2024-09 | Work automation with Claude begins — Practical automation — RPA, BI, report processing. The operating know-how of working with an AI, which everything later builds on, starts accumulating here. |
| 2025-03 | **MeaningSpace concept — the direction flips** — Stop fitting the AI into the human's file structure; let the human enter the AI's meaning space instead. Development of a personal AI memory OS begins, with subtractive design (remove the noise and meaning crystallizes) as its first principle. |

## Era 2 — A semantic memory OS takes shape
| Date | Event |
|---|---|
| 2026-01-02 | **The current DuckDB crystal database goes live (first crystal)** — Day one of the schema that stores conversations as crystals. It grew to 1,983 crystals by 2026-07-16. |
| 2026-05-16 | Multi-agent organizational OS concept written down — The idea of running several AI agents as an organization on top of MeaningSpace is crystallized. |
| 2026-06-04 – 06-07 | QIS (Quantum Inspired Semantic Space): design to Phase 0+1 — Success and failure vectors (posi_vec / nega_vec) back-filled for every crystal; the foundation of interference scoring implemented. |
| 2026-06-05 – 06-07 | SubtractLab brand established, subtractlab.com launched — Published on GitHub Pages (deployed 06-07), registered in Search Console, sitemap submitted. |
| 2026-06-11 | QIS interference formula, Model 2 — A combined formula — proximity as the main axis, plus a bonus for excess success and a penalty for excess failure — validated on real data. |
| 2026-06-13 | Crystallization fully mechanized — manual raw input removed — The path for raw data copied from the screen was closed; everything now flows through a pipeline that starts from the conversation logs. |

## Era 3 — A commander, and self-improvement
| Date | Event |
|---|---|
| 2026-07-04 | Sub-agent practice v2 — Chain, Swarm and Loop — When to run work in sequence, in parallel or in verification loops, and an escalation ladder from light to stronger models, written down as operating rules. |
| 2026-07-05 – | Clara bridge — a file-queue bridge between two AIs — A two-way bridge with another AI (Clara), built on a file queue and CDP monitoring; designed and partly implemented. |
| 2026-07-08 | **Self-learning pipeline (SelfEval → EWMA → self_preferences)** — The self-evaluation of every conversation is accumulated with decay and worn automatically as behavioral norms at the next boot. The same day, SelfRepair was designed (a repair task is filed automatically when a weakness score drops to −3.0 or below), four structural defects in the commander were fixed and Loop was formalized. |
| 2026-07-11 | self_preferences v8; cost structure measured — The cost of the API-billed route and the web-subscription route were measured side by side, and the DP route was made the default. |

## Era 4 — DP multi-agent (orchestrating web Claude)
| Date | Event |
|---|---|
| 2026-07-13 | **DP multi-agent foundation — five CDP lanes** — One lane = one Chrome = one profile = one CDP port. Findings fixed by measurement: an account-wide concurrency limit, 2.5-second staggered starts, the order for stopping zombie responses (three generations stopped in 3.6 s), persona contamination from user settings blocked by a neutralizing header, a split where Python touches files and DP decides, and no delete permission. The same day, all eight steps of the AutoCrystallize DP route were demonstrated. |
| 2026-07-14 | **Made permanent — dp_lease, dp_journal, dp_swarm, COMMANDER_PLAYBOOK** — A global slot lock across processes (ticket files, stale recovery after 15 minutes), a structured run journal, no more decisions based on UI strings (moved to DOM attributes), a Haiku production preset (deterministic check → retry on the same model → escalate), and a decision table for the commander. dp_swarm.py benchmark 4/4 PASS, 9–15 s per item, ¥0 extra cost. |
| 2026-07-15 | **Active coding loop in real use** — The commander runs its own checks and sends fixes back to a DP chat lane in an evaluator-optimizer loop; DP implemented the F6 flow hook v2 (mechanical detection of answers that skip memory). dp_swarm completed, response cleaning made permanent. Even the system manual was written by DP. |
| 2026-07-16 | **This timeline and the full architecture published** — The whole structure — DP multi-agent, self-learning, self-repair, active coding — illustrated on [Architecture](architecture.html). |

## Era 5 — Addresses for meaning, and public records
| Date | Event |
|---|---|
| 2026-09-01 | SweepSearch retired — one search path — Lexical search (BM25) and vector search fused by rank into a single search; from a result you descend into the section and read it. |
| 2026-09 | Line-level addresses for every crystal section — Every section of a conversation crystal carries the address of the log lines it came from. The model does not recall addresses; it selects them from a closed candidate set. |
| 2026-09-21 | **A tool that lights up skills** — Skills (procedures) are returned — title and a query to read them, nothing more — only when their similarity to the task clears a 0.80 threshold. Bundling skills into search results stopped. |
| 2026-10-04 | **Progress map — a map of files and a change ledger with reasons** — The present state of files and code is kept as a map; every change adds a tag, a reason and a reverse patch to a ledger. The tag stays in the conversation log and is linked to the conversation section when you look. No git. |
| 2026-10-07 | **Designs published as repositories (1–2)** — [meaningspace](https://github.com/subtractlab/meaningspace) and [ai-native-groupware](https://github.com/subtractlab/ai-native-groupware) published as dated public records of the design. |
| 2026-10-24 | The skill catalog leaves the prompt — The 25-line skill catalog in the always-loaded profile was removed — after checking that each of the 25 skills lights up within the top 3 for its own task. |
| 2026-11-07 | **Designs published (3–4) and the site rebuilt** — [progress-map](https://github.com/subtractlab/progress-map) and [threshold-skills](https://github.com/subtractlab/threshold-skills) published. subtractlab.com rebuilt as readable HTML in a single washi-and-sumi design on a golden-ratio grid. |

---
*Every addition is dated by its commit. Evidence that entries were not altered: git history, GitHub Pages deploy records and search-engine index dates.*
