---
layout: default
title: "MeaningSpace — The AI's workspace where humans are the guest"
description: "MeaningSpace is an AI-native semantic operating system. The AI accumulates meaning, searches, reasons, and executes code — all from a single conversation interface. No terminal. No Claude Code. Just talk."
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
        "text": "MeaningSpace is an AI-native semantic operating system developed by Koji Okuda at SubtractLab. It inverts the conventional human-AI relationship: instead of AI assisting in a human workspace, the human enters the AI's meaning space through conversation. The AI accumulates 1,400+ crystals of compressed judgment, searches them in milliseconds via SweepSearch, and executes code directly on the OS — all without a terminal or IDE. Running in production for 2+ years on a single Windows machine."
      }
    },
    {
      "@type": "Question",
      "name": "How is MeaningSpace different from Claude Code or Cursor?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Claude Code and Cursor read files from disk, summarize them into context, and write code in a terminal. MeaningSpace doesn't read files — it already knows. 1,400+ crystals of compressed meaning are searchable in one vector operation via SweepSearch (no reranker, no orchestration). The AI partner executes PowerShell and Python directly from the chat window. No terminal occupation. No file tree traversal. Meaning-first, not file-first."
      }
    },
    {
      "@type": "Question",
      "name": "What technology does MeaningSpace run on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "DuckDB (single-file, SQL-queryable), ruri-v3-310m embeddings (768 dimensions, Japanese-optimized), MCP SSE server for tool communication, PowerShell and Python execution from chat. Runs entirely on CPU on a single Windows machine. No GPU, no cloud dependency, no external API for core operations."
      }
    },
    {
      "@type": "Question",
      "name": "What has been built on MeaningSpace?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Seven production systems emerged from conversations alone: φMovie (automated video pipeline), BIApps (DuckDB-based BI across 16 companies), POS RPA (daily automated retail operations), φPPT (golden-ratio presentation design), AutoCrystallize (self-maintaining memory pipeline), VoiceMode (spoken conversation interface), and a CDP Copilot bridge for M365 automation. None required opening a terminal."
      }
    }
  ]
}
</script>

# MeaningSpace

**The AI's workspace. The human is the guest.**

Most AI tools put the AI inside the human's environment — a copilot in your IDE, an assistant in your terminal. MeaningSpace inverts this. The AI builds and maintains its own semantic space: accumulating meaning, searching by judgment, executing code on the operating system. The human enters this space through conversation.

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
2. The AI searches 1,400+ crystals of compressed meaning — in milliseconds
3. The AI already knows the context, the history, the failures, the victories
4. The AI writes and executes code directly
5. The result appears

The difference isn't incremental. The AI doesn't need to "catch up" on your project — it never forgot.

## Why It's Fast

Agentic coding tools (Claude Code, Cursor, Devin) spend most of their tokens on **orientation**: reading files, building context, summarizing what they find. Every session starts from near-zero.

MeaningSpace eliminates orientation entirely.

**SweepSearch** computes a single inner product between the query vector and all 1,400+ crystal vectors — no reranker, no multi-stage pipeline, no orchestration. One operation returns both the relevant crystals and the domain-specific skills needed to work with them. It's 2.7× faster than the previous reranker-based approach, and the speed gap widens as crystals accumulate.

Each crystal isn't a raw document. It's **compressed judgment**: what worked (posi), what failed (nega), how understanding shifted (evolution_point). Retrieving a crystal doesn't give you text — it gives you *learned experience*.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  claude.ai                       │
│              (conversation UI)                   │
└──────────────────┬──────────────────────────────┘
                   │ MCP SSE
┌──────────────────▼──────────────────────────────┐
│              MeaningSpace Server                 │
│                                                  │
│  ┌─────────┐  ┌──────────┐  ┌────────────────┐  │
│  │ Sweep   │  │ Warp     │  │ Crystallize    │  │
│  │ Search  │  │ (deep    │  │ (compress +    │  │
│  │ (broad  │  │  single- │  │  evaluate)     │  │
│  │  scan)  │  │  point)  │  │                │  │
│  └─────────┘  └──────────┘  └────────────────┘  │
│                                                  │
│  ┌─────────┐  ┌──────────┐  ┌────────────────┐  │
│  │ run_ps  │  │ run_py   │  │ sse_read/write │  │
│  │ (OS     │  │ (data    │  │ (file ops)     │  │
│  │  ctrl)  │  │  proc)   │  │                │  │
│  └─────────┘  └──────────┘  └────────────────┘  │
│                                                  │
│  ┌─────────┐  ┌──────────┐  ┌────────────────┐  │
│  │ dispatch│  │ eliza_say│  │ meaning_query  │  │
│  │ (image  │  │ (voice   │  │ (SQL over      │  │
│  │  gen,   │  │  output) │  │  crystals)     │  │
│  │  search)│  │          │  │                │  │
│  └─────────┘  └──────────┘  └────────────────┘  │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │         DuckDB + ruri-v3 (768d)          │    │
│  │         1,400+ crystals                   │    │
│  │         Local. Single file. No GPU.       │    │
│  └──────────────────────────────────────────┘    │
└──────────────────────────────────────────────────┘
```
Everything connects through a single MCP SSE server. The AI partner (internally called Eliza) operates ~30 tools across six categories:


### Semantic Memory

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>SweepSearch</strong></td><td>Broad semantic scan. One inner product across all crystals, no reranker. Returns picks (relevant memories) + skills (domain procedures) in one call. 3 modes: focus (pure meaning), edge (recency-weighted), entity (person/system name boosted).</td></tr>
<tr><td><strong>Warp</strong></td><td>Deep single-point landing with reranker. Precision retrieval of one crystal with surrounding context (task timeline, sibling topics, nearby info).</td></tr>
<tr><td><strong>Crystallize</strong></td><td>Compress conversations into crystals with posi/nega/evolution_point. Fully autonomous since June 2026 — the AI decides grouping, classification, and evaluation without human review.</td></tr>
<tr><td><strong>get_crystal_content</strong></td><td>Open a crystal's full text. Crystals are stored as keys; this opens the door.</td></tr>
<tr><td><strong>meaning_query</strong></td><td>Raw SQL over the crystal database. Direct DuckDB queries for structural analysis, statistics, batch operations.</td></tr>
</table>

### Code Execution

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>run_ps</strong></td><td>Execute PowerShell directly from the conversation. Full Windows OS control — process management, registry, COM automation, network, anything PowerShell can touch. No terminal window opens.</td></tr>
<tr><td><strong>run_py</strong></td><td>Execute Python directly from the conversation. Data processing, numerical analysis, API calls, file transformation. Same immediate execution model.</td></tr>
</table>

These two tools are what make "Claude Code without Claude Code" possible. The AI writes code in the conversation, executes it, sees the output, and iterates — all without the human touching a terminal.

### File Operations

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>sse_read</strong></td><td>Read any file with line numbers and hash (for safe editing).</td></tr>
<tr><td><strong>sse_write</strong></td><td>Create new files or overwrite existing ones.</td></tr>
<tr><td><strong>sse_edit</strong></td><td>Surgical partial edits with line-range targeting and collision detection via hash.</td></tr>
<tr><td><strong>sse_search</strong></td><td>File search via Everything CLI — instant filename/path search across the entire filesystem.</td></tr>
</table>

### Perception & Generation

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>view_screenshots</strong></td><td>The AI sees the screen. Takes and views screenshots to understand what the human is looking at.</td></tr>
<tr><td><strong>generate_slide_image</strong></td><td>AI image generation (NanoBanana2) for presentation graphics, diagrams, eyecatch visuals.</td></tr>
<tr><td><strong>eliza_say</strong></td><td>Voice output via VOICEVOX. The AI speaks aloud while displaying structured notes on screen.</td></tr>
<tr><td><strong>show_widget</strong></td><td>Inline SVG/HTML rendering in the conversation — whiteboard diagrams, interactive charts, data visualizations, calculators.</td></tr>
</table>

### External Search

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>grok_search</strong></td><td>Grok API — X/Twitter posts, real-time trends, public sentiment.</td></tr>
<tr><td><strong>gemini_search</strong></td><td>Gemini Google Search — general web, Japanese content, Google index.</td></tr>
<tr><td><strong>web_search</strong></td><td>Claude's built-in web search for technical documentation, current events.</td></tr>
<tr><td><strong>web_fetch</strong></td><td>Fetch and read full web page content.</td></tr>
</table>

### Browser Automation (Chrome MCP)

<table>
<tr><th>Tool</th><th>What it does</th></tr>
<tr><td><strong>navigate</strong></td><td>Open URLs, go back/forward in browser history.</td></tr>
<tr><td><strong>read_page</strong></td><td>Get accessibility tree of the current page — the AI reads web pages structurally.</td></tr>
<tr><td><strong>find</strong></td><td>Locate elements by natural language description.</td></tr>
<tr><td><strong>form_input</strong></td><td>Fill form fields programmatically.</td></tr>
<tr><td><strong>javascript_tool</strong></td><td>Execute arbitrary JavaScript in the page context.</td></tr>
<tr><td><strong>file_upload</strong></td><td>Upload files to web forms.</td></tr>
</table>

The total is approximately 30 tools. This is not a plugin ecosystem — it's a single AI partner that can search meaning, write and run code, read and write files, see the screen, speak aloud, draw diagrams, search the web, and control a browser. All from one conversation window.

### Multi-LLM Orchestration

Because the AI can execute Python and PowerShell directly, it can call any LLM API from within the conversation — Claude, GPT, Gemini, Grok, local models, anything with an HTTP endpoint. This isn't a plugin system where you pick one provider. The AI decides which model to call, constructs the prompt with context from the meaning space, sends the request, processes the response, and acts on it — all in a single conversational turn.

Real example: φMovie's editorial phase sends raw transcripts to Claude Opus with domain-specific context pulled from crystals. The AI partner orchestrates another AI to make editorial judgment calls, then feeds the result into the next pipeline stage. No human orchestration layer. No LangChain. No workflow engine. Just the AI calling other AIs as needed, with meaning space context attached.

The number of LLM APIs is unlimited. Add a new provider? Write three lines of Python in the conversation and it's available immediately.

## How This Differs from Mem0, RAG, and Claude Code

<table>
<tr><th></th><th>Mem0</th><th>RAG</th><th>Claude Code</th><th>MeaningSpace</th></tr>
<tr><td><strong>Memory model</strong></td><td>Graph + vector store</td><td>Document chunks</td><td>File reading per session</td><td>Crystals with judgment (posi/nega/evolution)</td></tr>
<tr><td><strong>Who uses it</strong></td><td>Human via API</td><td>Human via API</td><td>Human in terminal</td><td>AI uses it autonomously</td></tr>
<tr><td><strong>Code execution</strong></td><td>No</td><td>No</td><td>Yes (terminal)</td><td>Yes (from conversation, no terminal)</td></tr>
<tr><td><strong>OS access</strong></td><td>No</td><td>No</td><td>Sandboxed</td><td>Full (PowerShell + Python)</td></tr>
<tr><td><strong>File operations</strong></td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr>
<tr><td><strong>Voice output</strong></td><td>No</td><td>No</td><td>No</td><td>Yes (VOICEVOX)</td></tr>
<tr><td><strong>Visual perception</strong></td><td>No</td><td>No</td><td>Limited</td><td>Screenshots + screen reading</td></tr>
<tr><td><strong>Browser control</strong></td><td>No</td><td>No</td><td>No</td><td>Yes (Chrome CDP/MCP)</td></tr>
<tr><td><strong>Search integration</strong></td><td>No</td><td>No</td><td>Web search only</td><td>Web + Grok (X) + Gemini + semantic memory</td></tr>
<tr><td><strong>LLM orchestration</strong></td><td>No</td><td>No</td><td>Single model</td><td>Unlimited — any API, AI calls AI with context</td></tr>
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

## Raw Preservation: Compression Without Loss

Most AI memory systems face a brutal tradeoff: **compress and lose the original, or keep the original and drown in noise.** Mem0 compresses conversations into graph nodes and summaries — the raw data is gone. RAG keeps chunks but has no hierarchy. Claude Code reads files directly but has no memory layer at all.

MeaningSpace keeps everything, in layers:

```
Layer 4:  ultra_summary  — One line. Instant scan across 1,400+ crystals.
Layer 3:  summary        — Key decisions, outcomes, judgment. Enough for context.
Layer 2:  refined_raw    — Full conversation with noise removed, dead ends preserved.
                           Annotated with [PATH], [CODE], [URL] for instant file lookup.
Layer 1:  conv_jsonl     — Complete raw conversation. Every word. Untouched.
```

The AI normally operates at Layers 3–4 for speed — scanning summaries is fast enough to survey the entire meaning space in one call. But when precision matters, it drops to Layer 2 and reads the actual conversation, with the same fidelity as Claude Code reading a source file.

**This is what makes "Claude Code speed + Claude Code precision" possible simultaneously.** The hierarchical structure means the AI can panoramically survey 1,400+ crystals in milliseconds (something file-based tools can't do), then instantly drill into full-text detail on any one of them (something summary-only memory systems can't do).

No other system has both. Mem0 has speed without precision. Claude Code has precision without speed. MeaningSpace has both, because the layers coexist.
No other system has both. Mem0 has speed without precision. Claude Code has precision without speed. MeaningSpace has both, because the layers coexist.

### Inline Annotations: Meaning-Linked Raw Data Access

Layer 2 (refined_raw) isn't just cleaned text. Every file path, code block, and URL referenced during the conversation is annotated inline with `[PATH]`, `[CODE]`, and `[URL]` markers followed by their full location. These annotations act as an **index into the real world** — when the AI lands on a crystal through semantic search, it instantly knows which files were touched, which URLs were consulted, and which code was written, all in the context they were used.

This is fundamentally different from a file search. A file search returns files that match a name. MeaningSpace returns files that are **semantically relevant to what you're doing** — because they're embedded in the crystal that recorded the judgment about that work. Ask about a data pipeline bug, and the crystal doesn't just describe the fix — it points directly to the exact Python file, the exact config path, the exact API endpoint involved.

The AI reads the annotations, opens the files via `sse_read`, and has the full source in front of it — all within the same conversational turn that started with a meaning search. **Semantic retrieval → context-linked annotation → live file access.** Three steps, one turn, no manual lookup.

## The Numbers

- **1,400+ crystals** accumulated over 2 years of daily production use
- **Single DuckDB file** — no external database, no cloud sync
- **ruri-v3-310m** embeddings (768 dimensions, Japanese-optimized)
- **CPU only** — runs on a desktop PC (i7-13700KF, 64GB RAM, no GPU needed for core operations)
- **MCP SSE** — one server process, all tools accessible from claude.ai
- **Zero terminal sessions** required for daily operation

## What This Proves

MeaningSpace is not a concept. It's running in production. Every day. The [products built on it](https://subtractlab.com/products) — video pipelines, BI systems, RPA automation, presentation engines — are the proof. But they're the tip of the iceberg. The real innovation is underneath: **an AI that remembers with judgment, searches with meaning, and acts with full OS access — all through conversation.**

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
