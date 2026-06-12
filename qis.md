---
layout: default
title: "QIS — Quantum Inspired Semantic Space"
description: "QIS replaces similarity-based AI retrieval with interference scoring. Successes amplify, failures cancel. Search becomes computation, not lookup."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is QIS (Quantum Inspired Semantic Space)?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "QIS is a retrieval method for AI memory systems that replaces similarity matching with interference scoring. Developed by Koji Okuda at SubtractLab, it embeds success (posi) and failure (nega) vectors alongside each memory crystal, then computes an interference score at retrieval time. Memories where the query topic succeeded rise in ranking; memories where it failed drop or surface as warnings."
      }
    },
    {
      "@type": "Question",
      "name": "How does QIS differ from standard vector search?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standard vector search returns the most similar result. But similarity does not equal value — a memory about a catastrophic failure is just as 'similar' to a query as a memory about a breakthrough. QIS adds judgment: the interference score weighs similarity against success/failure evaluation and evolution depth. The result is the most meaningful memory, not just the closest one."
      }
    },
    {
      "@type": "Question",
      "name": "Does QIS require a GPU?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. QIS is implemented as CPU dot products on two additional vector columns (posi_vec, nega_vec) per crystal, computed within a single DuckDB SQL query. No GPU, no external inference service, no infrastructure change required."
      }
    },
    {
      "@type": "Question",
      "name": "What is the interference formula?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "interference_score = (posi_similarity - nega_similarity) x evolution_weight x vector_proximity. A crystal where the query topic succeeded amplifies (rises in ranking). A crystal where the query topic failed cancels (drops or surfaces as a warning). A crystal with a large evolution_point carries more weight regardless of direction."
      }
    },
    {
      "@type": "Question",
      "name": "Why is it called 'quantum inspired'?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The name draws from quantum mechanics' interference principle — where wave functions constructively or destructively interfere. In QIS, success and failure vectors interfere at retrieval time, producing amplification or cancellation. This is a conceptual analogy applied to semantic space, not a quantum computing implementation."
      }
    }
  ]
}
</script>

# QIS — Quantum Inspired Semantic Space

**Search that computes instead of matching. Retrieval becomes reasoning.**

QIS is the retrieval engine of [MeaningSpace](https://subtractlab.com/meaningspace). It replaces standard vector similarity search with interference-based scoring, making AI memory retrieval an act of computation rather than simple lookup.

## The Problem: Similarity Is Not Value

Every AI retrieval system — from RAG pipelines to vector databases to AI memory stores — uses the same approach: find the most similar result. Cosine similarity, dot product, nearest neighbor. The closest match wins.

But similarity does not equal value. A memory about a catastrophic failure is mathematically just as "similar" to a query as a memory about a breakthrough. The retrieval system cannot tell the difference. It returns the closest match, blind to whether that match represents success or disaster.

## Interference Scoring

QIS adds judgment to retrieval. Every crystal in MeaningSpace carries two additional vectors:

- **posi_vec** — embedding of what worked (the success evaluation)
- **nega_vec** — embedding of what failed (the failure evaluation)

At retrieval time, QIS computes:

**interference_score = (posi_similarity − nega_similarity) × evolution_weight × vector_proximity**

- A crystal where the query topic **succeeded** → amplifies (rises in ranking)
- A crystal where the query topic **failed** → cancels (drops, or surfaces as a warning)
- A crystal with a large **evolution_point** → carries more weight regardless of direction

The result: the AI retrieves the most *meaningful* memory, not just the most *similar* one.

## Why "Quantum Inspired"?

The name draws from quantum mechanics' interference principle — where wave functions constructively or destructively interfere. In QIS, success and failure vectors interfere at retrieval time. This is a conceptual analogy applied to semantic space, not a quantum computing implementation.

The parallel with existing academic work on quantum-inspired information retrieval (van Rijsbergen, Widdows) is acknowledged. QIS differs in that it applies interference to AI-authored evaluation vectors (posi/nega), not to term-document relationships.

## Implementation

Minimal infrastructure. Two additional FLOAT[1024] columns per crystal in DuckDB. CPU dot products. A single SQL query. No GPU. No external service.

QIS operates within the [3Gravity Architecture](https://subtractlab.com/3gravity) that structures MeaningSpace's memory at Crystal, Cluster, and Galaxy scales.

## Explore SubtractLab

- [MeaningSpace](https://subtractlab.com/meaningspace)
- [3Gravity Architecture](https://subtractlab.com/3gravity)
- **QIS** — you are here
- [SweepSearch](https://subtractlab.com/sweepsearch)
- [FAQ](https://subtractlab.com/faq)
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.