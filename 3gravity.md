---
layout: default
title: "3Gravity Architecture — Self-organizing AI memory structure"
description: "3Gravity Architecture organizes AI memory through semantic gravity at three scales: Crystal, Cluster, and Galaxy. No folders, no tags — structure emerges from meaning."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is 3Gravity Architecture?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "3Gravity Architecture is a self-organizing memory structure for AI systems, developed by Koji Okuda at SubtractLab. It organizes AI memories at three fractal scales — Crystal (single conversation), Cluster (thematic group), and Galaxy (domain/project family) — using vector proximity instead of folders or tags. Structure emerges from semantic gravity, like constellations forming through gravitational pull."
      }
    },
    {
      "@type": "Question",
      "name": "How does 3Gravity compare to traditional knowledge management?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Traditional knowledge management uses folders, tags, and categories — structures that require human maintenance and break down at scale. 3Gravity uses vector embeddings to let memories self-organize by meaning. No taxonomy needed. Opposing approaches to the same problem coexist at different distances from a query point without forcing resolution."
      }
    },
    {
      "@type": "Question",
      "name": "Why is it called 3Gravity?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The name refers to three scales of gravitational organization: Crystal (atomic unit), Cluster (thematic neighborhood), and Galaxy (strategic domain). Like physical gravity, structure emerges naturally from proximity rather than being imposed by labels. The architecture draws from the observation that natural systems self-organize without categories."
      }
    },
    {
      "@type": "Question",
      "name": "How does 3Gravity reduce token usage in AI systems?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Instead of stuffing a full conversation history into the context window, 3Gravity lets the AI navigate to the right cluster and read at the right resolution — ultra_summary for orientation, summary for context, refined_raw for depth. This compression at the architecture level replaces expansion at the token level, resulting in fewer tokens and better relevance."
      }
    }
  ]
}
</script>

# 3Gravity Architecture

**Self-organizing AI memory. No folders, no tags — structure emerges from meaning.**

3Gravity Architecture is the organizational backbone of [MeaningSpace](https://subtractlab.com/meaningspace). It replaces traditional knowledge management approaches — folders, tags, categories, databases — with a system where AI memories self-organize through semantic gravity at three fractal scales.

## The Problem: Categories Don't Scale

Every AI memory system and knowledge management tool faces the same problem: how do you organize thousands of memories? The standard answer is categories, tags, or folder structures. These require human maintenance, create artificial boundaries between related ideas, and break down as volume grows.

3Gravity takes a different approach: **let structure emerge from meaning**.

## Three Scales

| Scale | What It Is | Resolution |
|-------|-----------|------------|
| **Crystal** | A single distilled conversation | Full structured record with posi/nega/evolution |
| **Cluster** | Related crystals drawn together by semantic proximity | Thematic patterns and skill knowledge |
| **Galaxy** | An entire domain or project family | Strategic direction and long-term trajectory |

No boundaries are declared. Clusters and galaxies emerge from vector proximity — observed through semantic distance, like constellations observed through gravitational pull. Two opposing approaches to the same problem coexist at different distances from a query point. The system doesn't force resolution.

## Multi-Resolution Reading

The key advantage over flat memory systems: the AI reads at the resolution it needs.

- **Galaxy level** — "What domains have I worked in?" → ultra_summaries only
- **Cluster level** — "What do I know about this topic?" → summaries with cluster context
- **Crystal level** — "What exactly happened in that session?" → full refined_raw

This means fewer tokens in the context window, not more. Compression at the architecture level replaces expansion at the token level.

## Technical Foundation

3Gravity runs on DuckDB with 1024-dimensional vector embeddings (e5-large). Cluster detection uses vector proximity with time-decay weighting. No GPU required — all operations are CPU dot products and SQL queries.

The architecture powers [MeaningSpace](https://subtractlab.com/meaningspace) and uses [QIS (Quantum Inspired Semantic Space)](https://subtractlab.com/qis) for interference-based retrieval.

## Explore SubtractLab

- [MeaningSpace](https://subtractlab.com/meaningspace)
- **3Gravity Architecture** — you are here
- [QIS](https://subtractlab.com/qis)
- [SweepSearch](https://subtractlab.com/sweepsearch)
- [FAQ](https://subtractlab.com/faq)
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.