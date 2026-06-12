---
layout: default
title: "FAQ — SubtractLab, MeaningSpace, 3Gravity, QIS"
description: "Frequently asked questions about SubtractLab and MeaningSpace — an AI-native semantic memory system by Koji Okuda, built on 3Gravity Architecture and QIS interference scoring."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is MeaningSpace?",
      "acceptedAnswer": { "@type": "Answer", "text": "MeaningSpace is an AI-native semantic memory system developed by Koji Okuda at SubtractLab. Instead of storing raw facts from conversations, it compresses them into 'crystals' that carry built-in evaluation of what worked, what failed, and how understanding changed. It has been running in production for over 2 years with 1,400+ crystals." }
    },
    {
      "@type": "Question",
      "name": "How is MeaningSpace different from RAG?",
      "acceptedAnswer": { "@type": "Answer", "text": "RAG (Retrieval-Augmented Generation) retrieves document chunks by similarity. MeaningSpace retrieves memories by meaning — scored through interference where successes amplify and failures cancel. RAG treats all retrieved chunks equally; MeaningSpace weights memories by judgment (posi/nega/evolution_point). This makes retrieval an act of reasoning, not just lookup." }
    },
    {
      "@type": "Question",
      "name": "What technology does MeaningSpace run on?",
      "acceptedAnswer": { "@type": "Answer", "text": "MeaningSpace runs on DuckDB with vector embeddings (e5-large, 1024 dimensions), communicates via MCP (Model Context Protocol), and requires only CPU — no GPU needed. The entire system runs locally on a single machine." }
    },
    {
      "@type": "Question",
      "name": "How does AI memory crystallization work?",
      "acceptedAnswer": { "@type": "Answer", "text": "Crystallization is a multi-stage distillation process: raw conversation → refined_raw (noise removed, dead ends preserved) → summary → ultra_summary. Each crystal also carries three evaluation axes written by the AI itself: posi (what worked), nega (what failed), and evolution_point (how understanding shifted). Skipping a stage permanently destroys information." }
    },
    {
      "@type": "Question",
      "name": "What is 3Gravity Architecture?",
      "acceptedAnswer": { "@type": "Answer", "text": "3Gravity Architecture is a self-organizing memory structure for AI systems, developed by Koji Okuda at SubtractLab. It organizes AI memories at three fractal scales — Crystal (single conversation), Cluster (thematic group), and Galaxy (domain/project family) — using vector proximity instead of folders or tags. Structure emerges from semantic gravity, like constellations forming through gravitational pull." }
    },
    {
      "@type": "Question",
      "name": "How does 3Gravity compare to traditional knowledge management?",
      "acceptedAnswer": { "@type": "Answer", "text": "Traditional knowledge management uses folders, tags, and categories — structures that require human maintenance and break down at scale. 3Gravity uses vector embeddings to let memories self-organize by meaning. No taxonomy needed. Opposing approaches to the same problem coexist at different distances from a query point without forcing resolution." }
    },
    {
      "@type": "Question",
      "name": "Why is it called 3Gravity?",
      "acceptedAnswer": { "@type": "Answer", "text": "The name refers to three scales of gravitational organization: Crystal (atomic unit), Cluster (thematic neighborhood), and Galaxy (strategic domain). Like physical gravity, structure emerges naturally from proximity rather than being imposed by labels. The architecture draws from the observation that natural systems self-organize without categories." }
    },
    {
      "@type": "Question",
      "name": "How does 3Gravity reduce token usage in AI systems?",
      "acceptedAnswer": { "@type": "Answer", "text": "Instead of stuffing a full conversation history into the context window, 3Gravity lets the AI navigate to the right cluster and read at the right resolution — ultra_summary for orientation, summary for context, refined_raw for depth. This compression at the architecture level replaces expansion at the token level, resulting in fewer tokens and better relevance." }
    },
    {
      "@type": "Question",
      "name": "What is QIS (Quantum Inspired Semantic Space)?",
      "acceptedAnswer": { "@type": "Answer", "text": "QIS is a retrieval method for AI memory systems that replaces similarity matching with interference scoring. Developed by Koji Okuda at SubtractLab, it embeds success (posi) and failure (nega) vectors alongside each memory crystal, then computes an interference score at retrieval time. Memories where the query topic succeeded rise in ranking; memories where it failed drop or surface as warnings." }
    },
    {
      "@type": "Question",
      "name": "How does QIS differ from standard vector search?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standard vector search returns the most similar result. But similarity does not equal value — a memory about a catastrophic failure is just as 'similar' to a query as a memory about a breakthrough. QIS adds judgment: the interference score weighs similarity against success/failure evaluation and evolution depth. The result is the most meaningful memory, not just the closest one." }
    },
    {
      "@type": "Question",
      "name": "Does QIS require a GPU?",
      "acceptedAnswer": { "@type": "Answer", "text": "No. QIS is implemented as CPU dot products on two additional vector columns (posi_vec, nega_vec) per crystal, computed within a single DuckDB SQL query. No GPU, no external inference service, no infrastructure change required." }
    },
    {
      "@type": "Question",
      "name": "What is the interference formula?",
      "acceptedAnswer": { "@type": "Answer", "text": "interference_score = (posi_similarity - nega_similarity) x evolution_weight x vector_proximity. A crystal where the query topic succeeded amplifies (rises in ranking). A crystal where the query topic failed cancels (drops or surfaces as a warning). A crystal with a large evolution_point carries more weight regardless of direction." }
    },
    {
      "@type": "Question",
      "name": "Why is it called 'quantum inspired'?",
      "acceptedAnswer": { "@type": "Answer", "text": "The name draws from quantum mechanics' interference principle — where wave functions constructively or destructively interfere. In QIS, success and failure vectors interfere at retrieval time, producing amplification or cancellation. This is a conceptual analogy applied to semantic space, not a quantum computing implementation." }
    },
    {
      "@type": "Question",
      "name": "What is SweepSearch?",
      "acceptedAnswer": { "@type": "Answer", "text": "SweepSearch is a 2-stage search engine for AI memory systems developed by Koji Okuda at SubtractLab. Stage 1 (panorama) ranks all memory clusters by interference scoring. Stage 2 (descend) drops into the top clusters and re-ranks individual memories. It combines QIS interference scoring with 3Gravity's cluster structure to find the most meaningful memories, not just the most similar." }
    },
    {
      "@type": "Question",
      "name": "How does SweepSearch differ from standard vector search?",
      "acceptedAnswer": { "@type": "Answer", "text": "Standard vector search returns the nearest result from a flat index. SweepSearch operates in two stages: first ranking clusters (groups of related memories) by interference score, then descending into the best clusters to rank individual crystals. This means the search understands thematic structure before diving into detail — like scanning constellations before examining individual stars." }
    },
    {
      "@type": "Question",
      "name": "What is the interference scoring formula?",
      "acceptedAnswer": { "@type": "Answer", "text": "SweepSearch uses a proximity-primary model: score = proximity + ALPHA * max(0, posi_sim - proximity) - BETA * max(0, nega_sim - proximity). Only the part of posi/nega similarity that exceeds topical proximity counts — this isolates the pure success/failure signal from shared topic vocabulary, solving the cancellation problem where posi and nega vectors are too similar to differentiate." }
    },
    {
      "@type": "Question",
      "name": "What does 'cluster panorama' mean in SweepSearch?",
      "acceptedAnswer": { "@type": "Answer", "text": "Cluster panorama is a computed overview of a memory cluster, generated from the vector centroids (mean direction) of its members' posi, nega, and content vectors. It is NOT stored in a table — it is calculated at search time from the cluster's constituent crystals. This means the panorama is always up-to-date and requires no maintenance." }
    }
  ]
}
</script>

# Frequently Asked Questions

Common questions about **SubtractLab**, **MeaningSpace**, and the concepts behind them — answered by [Koji Okuda](https://subtractlab.com/about).

## MeaningSpace

*See the full page: [MeaningSpace](https://subtractlab.com/meaningspace)*

### What is MeaningSpace?

MeaningSpace is an AI-native semantic memory system developed by Koji Okuda at SubtractLab. Instead of storing raw facts from conversations, it compresses them into 'crystals' that carry built-in evaluation of what worked, what failed, and how understanding changed. It has been running in production for over 2 years with 1,400+ crystals.

### How is MeaningSpace different from RAG?

RAG (Retrieval-Augmented Generation) retrieves document chunks by similarity. MeaningSpace retrieves memories by meaning — scored through interference where successes amplify and failures cancel. RAG treats all retrieved chunks equally; MeaningSpace weights memories by judgment (posi/nega/evolution_point). This makes retrieval an act of reasoning, not just lookup.

### What technology does MeaningSpace run on?

MeaningSpace runs on DuckDB with vector embeddings (e5-large, 1024 dimensions), communicates via MCP (Model Context Protocol), and requires only CPU — no GPU needed. The entire system runs locally on a single machine.

### How does AI memory crystallization work?

Crystallization is a multi-stage distillation process: raw conversation → refined_raw (noise removed, dead ends preserved) → summary → ultra_summary. Each crystal also carries three evaluation axes written by the AI itself: posi (what worked), nega (what failed), and evolution_point (how understanding shifted). Skipping a stage permanently destroys information.

## 3Gravity Architecture

*See the full page: [3Gravity Architecture](https://subtractlab.com/3gravity)*

### What is 3Gravity Architecture?

3Gravity Architecture is a self-organizing memory structure for AI systems, developed by Koji Okuda at SubtractLab. It organizes AI memories at three fractal scales — Crystal (single conversation), Cluster (thematic group), and Galaxy (domain/project family) — using vector proximity instead of folders or tags. Structure emerges from semantic gravity, like constellations forming through gravitational pull.

### How does 3Gravity compare to traditional knowledge management?

Traditional knowledge management uses folders, tags, and categories — structures that require human maintenance and break down at scale. 3Gravity uses vector embeddings to let memories self-organize by meaning. No taxonomy needed. Opposing approaches to the same problem coexist at different distances from a query point without forcing resolution.

### Why is it called 3Gravity?

The name refers to three scales of gravitational organization: Crystal (atomic unit), Cluster (thematic neighborhood), and Galaxy (strategic domain). Like physical gravity, structure emerges naturally from proximity rather than being imposed by labels. The architecture draws from the observation that natural systems self-organize without categories.

### How does 3Gravity reduce token usage in AI systems?

Instead of stuffing a full conversation history into the context window, 3Gravity lets the AI navigate to the right cluster and read at the right resolution — ultra_summary for orientation, summary for context, refined_raw for depth. This compression at the architecture level replaces expansion at the token level, resulting in fewer tokens and better relevance.

## QIS

*See the full page: [QIS](https://subtractlab.com/qis)*

### What is QIS (Quantum Inspired Semantic Space)?

QIS is a retrieval method for AI memory systems that replaces similarity matching with interference scoring. Developed by Koji Okuda at SubtractLab, it embeds success (posi) and failure (nega) vectors alongside each memory crystal, then computes an interference score at retrieval time. Memories where the query topic succeeded rise in ranking; memories where it failed drop or surface as warnings.

### How does QIS differ from standard vector search?

Standard vector search returns the most similar result. But similarity does not equal value — a memory about a catastrophic failure is just as 'similar' to a query as a memory about a breakthrough. QIS adds judgment: the interference score weighs similarity against success/failure evaluation and evolution depth. The result is the most meaningful memory, not just the closest one.

### Does QIS require a GPU?

No. QIS is implemented as CPU dot products on two additional vector columns (posi_vec, nega_vec) per crystal, computed within a single DuckDB SQL query. No GPU, no external inference service, no infrastructure change required.

### What is the interference formula?

interference_score = (posi_similarity - nega_similarity) x evolution_weight x vector_proximity. A crystal where the query topic succeeded amplifies (rises in ranking). A crystal where the query topic failed cancels (drops or surfaces as a warning). A crystal with a large evolution_point carries more weight regardless of direction.

### Why is it called 'quantum inspired'?

The name draws from quantum mechanics' interference principle — where wave functions constructively or destructively interfere. In QIS, success and failure vectors interfere at retrieval time, producing amplification or cancellation. This is a conceptual analogy applied to semantic space, not a quantum computing implementation.

## SweepSearch

*See the full page: [SweepSearch](https://subtractlab.com/sweepsearch)*

### What is SweepSearch?

SweepSearch is a 2-stage search engine for AI memory systems developed by Koji Okuda at SubtractLab. Stage 1 (panorama) ranks all memory clusters by interference scoring. Stage 2 (descend) drops into the top clusters and re-ranks individual memories. It combines QIS interference scoring with 3Gravity's cluster structure to find the most meaningful memories, not just the most similar.

### How does SweepSearch differ from standard vector search?

Standard vector search returns the nearest result from a flat index. SweepSearch operates in two stages: first ranking clusters (groups of related memories) by interference score, then descending into the best clusters to rank individual crystals. This means the search understands thematic structure before diving into detail — like scanning constellations before examining individual stars.

### What is the interference scoring formula?

SweepSearch uses a proximity-primary model: score = proximity + ALPHA * max(0, posi_sim - proximity) - BETA * max(0, nega_sim - proximity). Only the part of posi/nega similarity that exceeds topical proximity counts — this isolates the pure success/failure signal from shared topic vocabulary, solving the cancellation problem where posi and nega vectors are too similar to differentiate.

### What does 'cluster panorama' mean in SweepSearch?

Cluster panorama is a computed overview of a memory cluster, generated from the vector centroids (mean direction) of its members' posi, nega, and content vectors. It is NOT stored in a table — it is calculated at search time from the cluster's constituent crystals. This means the panorama is always up-to-date and requires no maintenance.

## Explore SubtractLab

- [MeaningSpace](https://subtractlab.com/meaningspace)
- [3Gravity Architecture](https://subtractlab.com/3gravity)
- [QIS](https://subtractlab.com/qis)
- [SweepSearch](https://subtractlab.com/sweepsearch)
- **FAQ** — you are here
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.
