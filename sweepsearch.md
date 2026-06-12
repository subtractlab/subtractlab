---
layout: default
title: "SweepSearch — 2-stage interference search for AI memory"
description: "SweepSearch is a 2-stage search that ranks clusters by interference scoring, then descends into top clusters to find the most meaningful memories. Built on QIS and 3Gravity Architecture."
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is SweepSearch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SweepSearch is a 2-stage search engine for AI memory systems developed by Koji Okuda at SubtractLab. Stage 1 (panorama) ranks all memory clusters by interference scoring. Stage 2 (descend) drops into the top clusters and re-ranks individual memories. It combines QIS interference scoring with 3Gravity's cluster structure to find the most meaningful memories, not just the most similar."
      }
    },
    {
      "@type": "Question",
      "name": "How does SweepSearch differ from standard vector search?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Standard vector search returns the nearest result from a flat index. SweepSearch operates in two stages: first ranking clusters (groups of related memories) by interference score, then descending into the best clusters to rank individual crystals. This means the search understands thematic structure before diving into detail — like scanning constellations before examining individual stars."
      }
    },
    {
      "@type": "Question",
      "name": "What is the interference scoring formula?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "SweepSearch uses a proximity-primary model: score = proximity + ALPHA * max(0, posi_sim - proximity) - BETA * max(0, nega_sim - proximity). Only the part of posi/nega similarity that exceeds topical proximity counts — this isolates the pure success/failure signal from shared topic vocabulary, solving the cancellation problem where posi and nega vectors are too similar to differentiate."
      }
    },
    {
      "@type": "Question",
      "name": "What does 'cluster panorama' mean in SweepSearch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cluster panorama is a computed overview of a memory cluster, generated from the vector centroids (mean direction) of its members' posi, nega, and content vectors. It is NOT stored in a table — it is calculated at search time from the cluster's constituent crystals. This means the panorama is always up-to-date and requires no maintenance."
      }
    }
  ]
}
</script>

# SweepSearch

**2-stage interference search. Scan the constellations, then descend into stars.**

SweepSearch is the search engine of [MeaningSpace](https://subtractlab.com/meaningspace). It combines [QIS interference scoring](https://subtractlab.com/qis) with [3Gravity's cluster structure](https://subtractlab.com/3gravity) into a 2-stage retrieval process that finds the most meaningful memories, not just the nearest vectors.

## Why 2 Stages?

Standard vector search operates on a flat index — every memory is equal, and the nearest one wins. But real knowledge has structure. Memories cluster around themes, projects, and domains. A search engine that understands this structure can make better decisions.

SweepSearch exploits this structure:

**Stage 1 — Panorama**: Rank all clusters by interference score. Each cluster's panoramic signature is computed from the vector centroids of its members — posi centroid, nega centroid, content centroid. No pre-stored summaries needed; the panorama is calculated at search time.

**Stage 2 — Descend**: Drop into the top-ranked clusters and re-rank individual crystals by their own interference scores. This narrows the search space while ensuring thematic relevance.

The result: the search first identifies *which domain of knowledge matters*, then finds *which specific memories within that domain are most meaningful*.

## The Interference Model

The original QIS formula `(posi_sim - nega_sim) × proximity` collapsed on real data — posi and nega vectors of the same crystal share topic vocabulary, so their similarities nearly cancel. SweepSearch uses a proximity-primary model that isolates the pure success/failure signal:

**score = proximity + α × max(0, posi_sim − proximity) − β × max(0, nega_sim − proximity)**

Only the component of posi/nega that *exceeds* topical proximity counts. The shared-topic component cancels against proximity, leaving only the judgment signal — success bonus or failure penalty beyond mere relevance.

## Implementation

Proven on 1,400+ real crystals. KMeans clustering (24 clusters, ~60 crystals each) on DuckDB-stored 1024-dimensional embeddings. The entire pipeline — clustering, embedding, scoring — runs on CPU. No GPU. No external service.

The system uses `intfloat/multilingual-e5-large` for embeddings, the same model that powers MeaningSpace's warp navigation.

## Relation to Other Concepts

- **[QIS](https://subtractlab.com/qis)** provides the interference scoring theory
- **[3Gravity Architecture](https://subtractlab.com/3gravity)** provides the Crystal → Cluster → Galaxy structure
- **SweepSearch** combines both into a working search engine

## Explore SubtractLab

- [MeaningSpace](https://subtractlab.com/meaningspace)
- [3Gravity Architecture](https://subtractlab.com/3gravity)
- [QIS](https://subtractlab.com/qis)
- **SweepSearch** — you are here
- [FAQ](https://subtractlab.com/faq)
- [About the author](https://subtractlab.com/about)

---

Developed by **[Koji Okuda](https://subtractlab.com/about)** at **[SubtractLab](https://subtractlab.com)**.

© 2024–2026 Koji Okuda / SubtractLab. All rights reserved.