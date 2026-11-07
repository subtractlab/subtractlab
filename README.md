# SubtractLab

**Subtractive design for AI-native work.** Architectures by 奥田剛司 (Koji Okuda), each published as a dated public record.

## Architectures

| Repository | The problem it solves |
|---|---|
| **[meaningspace](https://github.com/subtractlab/meaningspace)** | Every AI session starts from zero. Keep every conversation whole, load only the meaning — with line-level addresses back to the source. |
| **[ai-native-groupware](https://github.com/subtractlab/ai-native-groupware)** | Everyone writes, everyone reads — without a SaaS or a database server. One file per person on shared storage, DuckDB on every PC. |
| **[progress-map](https://github.com/subtractlab/progress-map)** | Where every file is now, and why it changed. Each edit carries a reason and a reverse patch, tied to the conversation that caused it — no git. |
| **[threshold-skills](https://github.com/subtractlab/threshold-skills)** | Keep dozens of AI procedures without even a catalog in the prompt. A skill lights up only when the task clears a similarity threshold. |

Each repository explains the problem, the mechanism and how it compares with what exists today. Implementations are not published.

**Longer write-ups:** [subtractlab.com](https://subtractlab.com) · [3Gravity](https://subtractlab.com/3gravity) · [QIS](https://subtractlab.com/qis) · [DP Multi-Agent](dp-multiagent.md) · [Prior-art timeline](timeline.md)

---

## Vision

1. **The AI's workspace, not the human's** — instead of putting AI inside human tools, people enter the AI's meaning space through conversation.
2. **Memory becomes reasoning** — every crystal carries its own judgment (what worked, what failed, what was overturned), and that judgment is used at retrieval time.
3. **AI-native organizational OS** — personal meaning spaces first; the *who* of every crystal is already stored as a column, so groups and organizations can share a common layer later.

## Other projects

All built through conversation on MeaningSpace. See **[Products](https://subtractlab.com/products)**.

- **φMovie** — automated video production pipeline
- **BIApps** — serverless BI on shared storage + local DuckDB (architecture: [ai-native-groupware](https://github.com/subtractlab/ai-native-groupware))
- **φPPT** — golden-ratio, AI-native presentation design
- **AutoCrystallize** — self-maintaining memory pipeline
- **VoiceMode** — spoken conversation interface (VOICEVOX)

## Changelog (dated anchors)

| Date | Milestone |
|---|---|
| 2026-06-06 | First public anchor — brand & site launch |
| 2026-07-08 | Self-learning pipeline + SelfRepair design |
| 2026-07-13 | DP multi-agent foundation |
| 2026-07-16 | Public disclosure: architecture.html / history.html / dp-multiagent.md / timeline.md |
| 2026-09-01 | SweepSearch retired; search moved to lexical + vector fusion with descend |
| 2026-09 | Line-level addresses for every crystal section (closed-set selection) |
| 2026-10-04 | Progress map: file map + change ledger with reasons and reverse patches |
| 2026-10-07 | MeaningSpace architecture published as its own repository: [subtractlab/meaningspace](https://github.com/subtractlab/meaningspace) |
| 2026-10-07 | AI Native Groupware architecture published: [subtractlab/ai-native-groupware](https://github.com/subtractlab/ai-native-groupware) |
| 2026-11-07 | Progress map published: [subtractlab/progress-map](https://github.com/subtractlab/progress-map) |
| 2026-11-07 | Threshold skills published: [subtractlab/threshold-skills](https://github.com/subtractlab/threshold-skills) |
| 2026-11-07 | subtractlab.com top page rebuilt as static, readable HTML (the visual tour moved to tour.html) |

Full dated history: **[timeline.md](timeline.md)**

## Author

**奥田剛司 (Koji Okuda)** · Independent builder. Subtractive design practitioner.

[subtractlab.com](https://subtractlab.com) · [@subtractlabo](https://x.com/subtractlabo) · [@SUBTRACTLAB](https://www.youtube.com/@SUBTRACTLAB) · [note.com/subtractlab](https://note.com/subtractlab)

*First public anchor: June 6, 2026. This README and all pages are timestamped by git commit history.*
