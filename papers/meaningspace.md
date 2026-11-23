---
layout: default
title: "MeaningSpace: Keep Every Word, Load Only the Meaning — paper"
description: "Paper (draft v0.2, 2026-11-20) by Koji Okuda. A lossless conversational memory with line-level addresses, threshold-gated skills, and a time-aware read layer."
citation_title: "MeaningSpace: Keep Every Word, Load Only the Meaning — A lossless conversational memory with line-level addresses, threshold-gated skills, and a time-aware read layer"
citation_authors:
  - "Okuda, Koji"
citation_date: "2026/11/20"
citation_doi: "10.5281/zenodo.24388336"
citation_institution: "SubtractLab"
citation_pdf: "/papers/meaningspace-okuda-2026-v0.2.pdf"
---

# MeaningSpace: Keep Every Word, Load Only the Meaning

**A lossless conversational memory with line-level addresses, threshold-gated skills, and a time-aware read layer**

Koji Okuda · SubtractLab · ORCID [0009-0003-9251-8455](https://orcid.org/0009-0003-9251-8455)

Draft v0.2 — 2026-11-20 — not peer reviewed

- **PDF:** [meaningspace-okuda-2026-v0.2.pdf](/papers/meaningspace-okuda-2026-v0.2.pdf)
- **DOI:** [10.5281/zenodo.24388336](https://doi.org/10.5281/zenodo.24388336)

## Abstract

Assistants that work with a person every day forget everything between sessions. The common remedies either summarize the history and discard the original, or reload and search the raw history on every question. We describe MeaningSpace, a local memory layer that takes a third path: the full conversation log is kept as an immutable, line-numbered ground, and a meaning layer of sections ("crystals") is placed on top of it. Every section records its outcome (decided / overturned / open) and the addresses of the log lines it was distilled from, so a new session loads only a few sections and can still descend to the exact original lines. Working procedures ("skills") live in the same layer and surface only when their similarity to the task clears a fixed threshold, so no skill catalog is ever placed in the prompt. The system has been in daily use by one builder since 2023; it now holds 4,722 conversations (1,567 imported from ChatGPT, the rest with Claude) and 35,789 sections, plus 78 skills. We report three measurements taken in November 2026 on the author's personal computer: (1) moving the read path from a single DuckDB file to a Parquet read layer reduced the median latency of one retrieval from 1,551 ms to 457 ms with identical top-5 results on 30 of 30 queries, shrank the data needed for retrieval from 2.3 GB to 157 MB, and allowed 5 concurrent readers to succeed on 50 of 50 reads while a writer held the database (0 of 50 before); (2) adding dates, a one-line summary and the newest same-topic conversation to each retrieval result raised the accuracy of memory-less agents on time-sensitive questions from 3/11 to 8/11 (Sonnet 5.5) and from 4/11 to 9/11 (Opus 5.5); (3) a second AI agent, treated as a second user, read the memory and edited code through the same host and passed the same procedure three times in a row. The evaluations are small and single-user; we state their limits explicitly.

## Cite

Okuda, K. (2026). *MeaningSpace: Keep Every Word, Load Only the Meaning — A lossless conversational memory with line-level addresses, threshold-gated skills, and a time-aware read layer* (Draft v0.2). SubtractLab. https://doi.org/10.5281/zenodo.24388336

## Design records

- AI Native Groupware: a dated design record — [10.5281/zenodo.24388288](https://doi.org/10.5281/zenodo.24388288)
- Threshold Skills: a dated design record — [10.5281/zenodo.24388292](https://doi.org/10.5281/zenodo.24388292)
- Progress Map: a dated design record — [10.5281/zenodo.24388290](https://doi.org/10.5281/zenodo.24388290)
- MeaningSpace: a dated design record — [10.5281/zenodo.24388285](https://doi.org/10.5281/zenodo.24388285)

---

[Back to MeaningSpace](https://subtractlab.com/meaningspace)
