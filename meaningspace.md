---
layout: default
title: "MeaningSpace — The AI's workspace where humans are the guest"
description: "MeaningSpace is an AI-native semantic operating system. The AI accumulates meaning, searches, reasons, and builds — all from a single conversation. No terminal. No Claude Code. No Codex. Just talk."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is MeaningSpace?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MeaningSpace is an AI-native semantic operating system developed by Koji Okuda at SubtractLab. It inverts the conventional human-AI relationship: instead of AI assisting in a human workspace, the human enters the AI's meaning space through conversation. The AI accumulates 4,600+ crystals of compressed judgment, searches them in milliseconds via SweepSearch, and does the work inside the same conversation — without a terminal, an IDE, Claude Code or Codex. Running in production for 2+ years."
      }
    },
    {
      "@type": "Question",
      "name": "How is MeaningSpace different from Claude Code or Cursor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Claude Code and Cursor read files from disk, summarize them into context, and write code in a terminal. MeaningSpace doesn't read files — it already knows. 4,600+ crystals of compressed meaning are searchable in one vector operation via SweepSearch (no reranker, no orchestration). The AI partner works inside MeaningSpace's own environment, directly from the chat window. No terminal. No file tree traversal. Meaning-first, not file-first."
      }
    },
    {
      "@type": "Question",
      "name": "What technology does MeaningSpace run on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "DuckDB (single-file, SQL-queryable), ruri-v3-310m embeddings (768 dimensions, Japanese-optimized), and a proprietary conversation-first environment built by SubtractLab. Runs on CPU. No GPU, no cloud dependency for core operations."
      }
    },
    {
      "@type": "Question",
      "name": "What has been built on MeaningSpace?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Seven production systems emerged from conversations alone: φMovie (automated video pipeline), BIApps (DuckDB-based BI), φPPT (golden-ratio presentation design), AutoCrystallize (self-maintaining memory pipeline), VoiceMode (spoken conversation interface). None required opening a terminal."
      }
    }
  ]
}
</script>

# MeaningSpace

**The AI's workspace. The human is the guest.**

Most AI tools put the AI inside the human's environment — a copilot in your IDE, an assistant in your terminal. MeaningSpace inverts this. The AI builds and maintains its own semantic space: accumulating meaning, searching by judgment, doing the work itself. The human enters this space through conversation.

No terminal. No IDE. No file tree traversal. Just talk.

## The Inversion

In conventional AI-assisted development:

1. The human opens a terminal or IDE
2. The AI reads files from disk
3. The AI summarizes what it found
4. The AI writes code
5. The human runs it

In MeaningSpace:

1. The human says what they want
2. The AI searches 4,600+ crystals of compressed meaning — in milliseconds
3. The AI already knows the context, the history, the failures, the victories
4. The AI does the work and checks it
5. The result appears

The difference isn't incremental. The AI doesn't need to "catch up" on your project — it never forgot.

## Why It's Fast

Agentic coding tools (Claude Code, Cursor, Devin) spend most of their tokens on **orientation**: reading files, building context, summarizing what they find. Every session starts from near-zero.

MeaningSpace eliminates orientation entirely.

**SweepSearch** computes a single inner product between the query vector and all 1,400+ crystal vectors — no reranker, no multi-stage pipeline, no orchestration. One operation returns both the relevant crystals and the domain-specific skills needed to work with them. It's 2.7× faster than the previous reranker-based approach, and the speed gap widens as crystals accumulate.

Each crystal isn't a raw document. It's **compressed judgment**: what worked (posi), what failed (nega), how understanding shifted (evolution_point). Retrieving a crystal doesn't give you text — it gives you *learned experience*.

## Architecture

One conversation window. Behind it, MeaningSpace — a proprietary environment built and run by SubtractLab. Not Claude Code, not Codex, not an IDE plugin. Inside it the AI partner (internally called Eliza) remembers, searches, builds and checks its own work.

How the environment is wired, and what it is allowed to touch, is deliberately not published. What is published is the memory model below.

### Semantic Memory

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>SweepSearch</strong></td><td>Broad semantic scan. One inner product across all crystals, no reranker. Returns picks (relevant memories) + skills (domain procedures) in one call. 3 modes: focus (pure meaning), edge (recency-weighted), entity (person/system name boosted).</td></tr>
<tr><td><strong>Warp</strong></td><td>Deep single-point landing with reranker. Precision retrieval of one crystal with surrounding context (task timeline, sibling topics, nearby info).</td></tr>
<tr><td><strong>Crystallize</strong></td><td>Compress conversations into crystals with posi/nega/evolution_point. Fully autonomous since June 2026 — the AI decides grouping, classification, and evaluation without human review.</td></tr>
<tr><td><strong>get_crystal_content</strong></td><td>Open a crystal's full text. Crystals are stored as keys; this opens the door.</td></tr>
<tr><td><strong>meaning_query</strong></td><td>Raw SQL over the crystal database. Direct DuckDB queries for structural analysis, statistics, batch operations.</td></tr>
</table>

### Making and checking

Writing, images, video, sites and code are produced inside the conversation and verified before they are reported. The AI also speaks aloud (VOICEVOX) while showing structured notes on screen.

## How This Differs from Mem0, RAG, and Claude Code

<table>
<tr><th></th><th>Mem0</th><th>RAG</th><th>Claude Code</th><th>MeaningSpace</th></tr>
<tr><td><strong>Memory model</strong></td><td>Graph + vector store</td><td>Document chunks</td><td>File reading per session</td><td>Crystals with judgment (posi/nega/evolution)</td></tr>
<tr><td><strong>Who uses it</strong></td><td>Human via API</td><td>Human via API</td><td>Human in terminal</td><td>AI uses it autonomously</td></tr>
<tr><td><strong>Where the work happens</strong></td><td>Your app</td><td>Your app</td><td>Terminal</td><td>The conversation (own environment)</td></tr>
<tr><td><strong>Voice output</strong></td><td>No</td><td>No</td><td>No</td><td>Yes (VOICEVOX)</td></tr>
<tr><td><strong>Raw data preservation</strong></td><td>No — compressed, originals discarded</td><td>Chunks only, no hierarchy</td><td>Files on disk, no memory</td><td>Full hierarchy: raw → refined → summary → ultra. Nothing lost</td></tr>
<tr><td><strong>Memory loop</strong></td><td>Store/retrieve</td><td>Retrieve only</td><td>None</td><td>Full loop: retrieve → act → crystallize → store</td></tr>
</table>

The fundamental difference: Mem0 and RAG are **memory backends that humans query**. Claude Code is a **coding tool that reads files**. MeaningSpace is an **operating system where the AI lives** — it remembers, reasons, acts, and learns, all autonomously. The human participates through conversation.
This is what makes it possible to do everything Claude Code does — and more — without ever opening a terminal.

**Raw conversation → Refined raw → Summary → Ultra-summary**

Each stage compresses further. No stage can be skipped — skipping permanently destroys information.

Every crystal carries three self-evaluation axes, written by the AI that did the work:

- **posi** — What succeeded: approaches that worked, tools that delivered
- **nega** — What failed: dead ends, wasted effort, wrong assumptions
- **evolution_point** — How understanding shifted: not progress, but *change in worldview*
This is why retrieval isn't lookup — it's computed reasoning. The AI doesn't just find similar memories. It finds memories whose *judgment* is relevant.

### QIS: Retrieval by Interference, Not Similarity

These three axes aren't just metadata. They are **searchable vectors**. When the AI searches for relevant memories, [QIS (Quantum Inspired Semantic Space)](https://subtractlab.com/qis) computes an interference score across posi, nega, and evolution_point — not just text similarity. A crystal whose failures are relevant to your current situation ranks higher than one that merely mentions the same topic. This is what no other memory system does: retrieve by *judgment relevance*, not keyword or embedding proximity alone.

### Fractal Organization: Scale × Kind

Crystals are not a flat list. They are organized along two orthogonal axes:

**Scale** (how big is this knowledge?):

- **Crystal** — A single conversation's distilled judgment
- **Cluster** — A group of crystals in the same domain (ClusterSkill: the accumulated "how to" of that domain)
- **Galaxy** — An entire domain of practice (e.g., all of MeaningSpace development, all of ledger work)

**Kind** (what type of knowledge?):

- **General** — Observations, decisions, discoveries
- **Skill** — Reusable domain procedures (ClusterSkills)
- **Project** — Ongoing work tracked by meaning proximity, not task boards
- **Task** — Specific action items, also tracked by semantic proximity

**Projects and tasks live in meaning space, not in a task manager.** There are no Kanban boards, no status fields, no manually maintained backlogs. A "project" is a cluster of crystals about related work. A "task" is a crystal that records what needs to be done and why. When the AI searches for "what's pending on φMovie," it finds the relevant task crystals by meaning — not by querying a status column. This means projects and tasks are automatically organized by semantic proximity, automatically inherit context from surrounding crystals, and never go stale because they exist in the same space as the work itself.

This is [3Gravity Architecture](https://subtractlab.com/3gravity) — fractal scales from Crystal to Galaxy, with each level self-similar in structure.

## Raw Preservation: Compression Without Loss

Most AI memory systems face a brutal tradeoff: **compress and lose the original, or keep the original and drown in noise.** Mem0 compresses conversations into graph nodes and summaries — the raw data is gone. RAG keeps chunks but has no hierarchy. Claude Code reads files directly but has no memory layer at all.

MeaningSpace keeps everything, in layers:

```
Layer 4:  ultra_summary  — One line. Instant scan across 4,600+ crystals.
Layer 3:  summary        — Key decisions, outcomes, judgment. Enough for context.
Layer 2:  refined_raw    — Full conversation with noise removed, dead ends preserved.
                           Annotated with [PATH], [CODE], [URL] for instant file lookup.
Layer 1:  conv_jsonl     — Complete raw conversation. Every word. Untouched.
```

The AI normally operates at Layers 3–4 for speed — scanning summaries is fast enough to survey the entire meaning space in one call. But when precision matters, it drops to Layer 2 and reads the actual conversation, with the same fidelity as Claude Code reading a source file.

**This is what makes "Claude Code speed + Claude Code precision" possible simultaneously.** The hierarchical structure means the AI can panoramically survey 4,600+ crystals in milliseconds (something file-based tools can't do), then instantly drill into full-text detail on any one of them (something summary-only memory systems can't do).

No other system has both. Mem0 has speed without precision. Claude Code has precision without speed. MeaningSpace has both, because the layers coexist.

### Inline Annotations: Meaning-Linked Raw Data Access

Layer 2 (refined_raw) isn't just cleaned text. Every file path, code block, and URL referenced during the conversation is annotated inline with `[PATH]`, `[CODE]`, and `[URL]` markers followed by their full location. These annotations act as an **index into the real world** — when the AI lands on a crystal through semantic search, it instantly knows which files were touched, which URLs were consulted, and which code was written, all in the context they were used.

The AI follows the annotations to the source and has it in front of it — all within the same conversational turn that started with a meaning search. **Semantic retrieval → context-linked annotation → live file access.** Three steps, one turn, no manual lookup.

## Unlimited Scale, Instant Panorama

Every AI system today hits a wall: the context window. 128K tokens. 200K tokens. Whatever the number, there's a ceiling. Past that ceiling, information is discarded, summarized away, or simply unavailable. The AI forgets.

MeaningSpace has no ceiling. Crystals live in DuckDB — a local database file that scales with your disk. 4,600 crystals today. 10,000 tomorrow. 100,000 next year. The structure doesn't change. The speed barely changes. SweepSearch computes one inner product per crystal — linear, no index fragmentation, no reranker overhead.

What makes this different from "just a bigger database" is the **multi-resolution panorama**:

- **Ultra-summary** — Survey all 4,600+ crystals in a single tool call. See the shape of everything.
- **Summary** — Drop into any crystal's key decisions, outcomes, and judgment.
- **Refined raw** — Read the full conversation with context-linked file annotations.
- **Conv_jsonl** — Access the complete raw conversation, every word, untouched.

And the panorama isn't limited to one angle:

- **Focus mode** (θ=0) — Pure semantic meaning. Find crystals by what they're about.
- **Edge mode** (θ=0.3) — Recency-weighted. Find the latest developments in a topic.
- **Entity mode** — Person/system name boosted. Find everything a specific person or tool touched.
- **SQL queries** — Direct DuckDB access for structural analysis across the entire crystal database.

This is what "freed from the context window" looks like. The AI doesn't fit your project into 128K tokens. It navigates 2 years of accumulated judgment — with raw data intact — in milliseconds, from any angle, at any resolution.


## The Numbers

- **4,600+ crystals** accumulated over 2 years of daily production use
- **Single DuckDB file** — no external database, no cloud sync
- **ruri-v3-310m** embeddings (768 dimensions, Japanese-optimized)
- **CPU only** — no GPU needed for core operations
- **One proprietary environment** — reached from the chat app
- **Zero terminal sessions** required for daily operation

## What This Proves

MeaningSpace is not a concept. It's running in production. Every day. The [products built on it](https://subtractlab.com/products) — video pipelines, BI systems, RPA automation, presentation engines — are the proof. But they're the tip of the iceberg. The real innovation is underneath: **an AI that remembers with judgment, searches with meaning, and acts with its own environment — all through conversation.**

## Explore SubtractLab

- **MeaningSpace** — you are here
- [Products built on MeaningSpace](https://subtractlab.com/products)
- [3Gravity Architecture](https://subtractlab.com/3gravity)
- [QIS](https://subtractlab.com/qis)
- [SweepSearch](https://subtractlab.com/sweepsearch)
- [FAQ](https://subtractlab.com/faq)
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.
