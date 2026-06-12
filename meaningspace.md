---
layout: default
title: "MeaningSpace — AI-native semantic memory system"
description: "MeaningSpace is an AI memory system that compresses conversations into crystals carrying success/failure judgment. Built on DuckDB. An alternative to RAG and vector-store memory."
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
        "text": "MeaningSpace is an AI-native semantic memory system developed by Koji Okuda at SubtractLab. Instead of storing raw facts from conversations, it compresses them into 'crystals' that carry built-in evaluation of what worked, what failed, and how understanding changed. It has been running in production for over 2 years with 1,400+ crystals."
      }
    },
    {
      "@type": "Question",
      "name": "How is MeaningSpace different from RAG?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "RAG (Retrieval-Augmented Generation) retrieves document chunks by similarity. MeaningSpace retrieves memories by meaning — scored through interference where successes amplify and failures cancel. RAG treats all retrieved chunks equally; MeaningSpace weights memories by judgment (posi/nega/evolution_point). This makes retrieval an act of reasoning, not just lookup."
      }
    },
    {
      "@type": "Question",
      "name": "What technology does MeaningSpace run on?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "MeaningSpace runs on DuckDB with vector embeddings (e5-large, 1024 dimensions), communicates via MCP (Model Context Protocol), and requires only CPU — no GPU needed. The entire system runs locally on a single machine."
      }
    },
    {
      "@type": "Question",
      "name": "How does AI memory crystallization work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Crystallization is a multi-stage distillation process: raw conversation → refined_raw (noise removed, dead ends preserved) → summary → ultra_summary. Each crystal also carries three evaluation axes written by the AI itself: posi (what worked), nega (what failed), and evolution_point (how understanding shifted). Skipping a stage permanently destroys information."
      }
    }
  ]
}
</script>

# MeaningSpace

**An AI-native semantic memory system. Memory through subtraction, not addition.**

MeaningSpace is an AI memory management system that takes a fundamentally different approach from conventional AI memory stores, RAG pipelines, and vector databases. Instead of scaling by storing more data, MeaningSpace scales by **compressing conversations into crystals that carry their own judgment** — what succeeded, what failed, and how understanding evolved.

## The Problem with Current AI Memory

Existing AI memory systems — from ChatGPT's memory to Mem0, Letta, and enterprise RAG solutions — extract facts and store them as flat key-value pairs. After hundreds of hours of collaboration, the AI remembers *what you said* but has no idea *what worked or what failed*. Every insight gets the same weight as every passing mention.

MeaningSpace solves this by making the AI that did the work also write the judgment about the work.

## How It Works

### Crystallization

Conversations are distilled through stages, each compressing further but never skipping:

**Raw conversation → Refined raw → Summary → Ultra-summary**

Each crystal carries three evaluation axes:

- **posi** — What worked: approaches that succeeded
- **nega** — What failed: dead ends, pitfalls, wasted effort
- **evolution_point** — How understanding shifted: not just progress, but change in worldview

### Semantic Navigation (not folder structure)

Crystals self-organize by vector proximity into clusters and galaxies — no folders, no tags, no categories. Navigation works like a telescope: zoom out for strategic direction, zoom in for operational detail. The AI loads only what matters at the resolution it needs.

### Interference-Based Retrieval (QIS)

Standard retrieval asks "which memory is most similar?" MeaningSpace asks "which memory is most meaningful?" Through [QIS (Quantum Inspired Semantic Space)](https://subtractlab.com/qis), successes amplify and failures cancel at retrieval time, making search an act of computation rather than lookup.

## Technical Stack

- **Storage**: DuckDB (local, single-file, SQL-queryable)
- **Embeddings**: e5-large (1024 dimensions)
- **Communication**: MCP (Model Context Protocol) via SSE/Streamable HTTP
- **Architecture**: [3Gravity Architecture](https://subtractlab.com/3gravity)
- **GPU**: Not required. Runs on CPU.

## Status

In production for 2+ years. 1,400+ crystals accumulated across software engineering, financial systems, video production, and conceptual research.

## Explore SubtractLab

- **MeaningSpace** — you are here
- [3Gravity Architecture](https://subtractlab.com/3gravity)
- [QIS](https://subtractlab.com/qis)
- [SweepSearch](https://subtractlab.com/sweepsearch)
- [FAQ](https://subtractlab.com/faq)
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.