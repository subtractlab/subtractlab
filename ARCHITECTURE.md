# 3Gravity Architecture

**Author: Koji Okuda** · First public anchor: June 6, 2026

---

## The Problem

Every major AI assistant now offers "memory." They extract facts from your conversations, store them as key-value pairs, and recall them later. This is useful — and fundamentally limited.

Here's what breaks:

- **Memory without judgment.** Current systems remember *what* you said, but not *what worked* and *what failed*. A year of conversations collapses into a flat list of facts, indistinguishable from each other.
- **Retrieval without computation.** Search returns the closest match by embedding distance. But closeness in vector space doesn't tell you which result led to a breakthrough and which led to a dead end. The system has no way to know.
- **Storage without structure.** Facts pile up without hierarchy. There's no difference between a passing mention and a hard-won insight. Everything sits at the same depth, at the same weight.

The result: AI memory systems today are filing cabinets with a search bar. They store. They retrieve. They don't *think*.

3Gravity Architecture is built on a different premise: **storage is computation**. Every unit of memory carries its own evaluation — what succeeded, what failed, how understanding changed — and that evaluation is used at retrieval time to rank, filter, and interfere. The act of remembering is itself an act of reasoning.

---

## How It Works

### Crystallization: Memory That Preserves Failure

A conversation is not summarized into a single note. It is *crystallized* — condensed through a multi-stage distillation that preserves what most systems discard:

```
raw conversation (everything, unmodified)
  → refined_raw (noise removed; dead ends, pivots, abandoned directions kept)
    → summary (compressed for search)
      → ultra_summary (maximum compression for galaxy-scale view)
```

Each stage takes only from the stage above. Skipping a stage permanently destroys information. This is deliberate: the dead ends and wrong turns are often more valuable than the conclusions.

Every crystal also carries three evaluation axes, written by the co-creating AI as a participant in the work — not extracted automatically:

| Axis | What it captures |
|------|-----------------|
| **posi** | What worked — technically successful approaches |
| **nega** | What failed — dead ends, pitfalls, time sinks |
| **evolution_point** | How understanding changed — not progress, but shift in worldview |

These are not metadata tags. They are embedded into vector space and used for computation at retrieval time.

### 3Gravity: Structure Without Labels

Crystals organize across three scales, like matter in the cosmos:

| Scale | What you see | How deep you read |
|-------|-------------|-------------------|
| **Crystal** | A single conversation's distilled output | refined_raw (full structured record) |
| **Cluster** | A group of related crystals | summary (thematic patterns) |
| **Galaxy** | An entire domain or project family | ultra_summary (strategic direction) |

The critical design choice: **no explicit boundaries**. Clusters and galaxies are not folders, categories, or tags. They emerge from vector proximity — observed through distance, never declared through labels. Like constellations: you don't draw borders. You observe gravitational pull.

This means contradictions coexist. Two opposing approaches to the same problem can live at different distances from the same query point. The system doesn't resolve the contradiction — it presents both, weighted by proximity.

### QIS: Retrieval as Interference

This is where storage becomes computation.

Standard semantic search returns results ranked by vector distance: *how similar is this memory to the query?* QIS adds a second dimension: *how much did this memory contribute to success or failure?*

The mechanism is structurally inspired by quantum interference. In quantum computing, correct computation paths amplify each other while incorrect paths cancel out. QIS applies the same principle:

```
interference_score = (posi_similarity - nega_similarity) × evolution_weight × vector_proximity
```

What this does in practice:

- A crystal where the query topic succeeded (high posi match) **amplifies** — it rises in ranking.
- A crystal where the query topic failed (high nega match) **cancels** — it drops, or surfaces with a warning.
- A crystal with a large evolution_point — where understanding fundamentally shifted — carries more weight regardless of direction.

The result: the system doesn't just find *related* memories. It finds memories that *matter* — the ones where real learning happened, weighted by whether that learning was toward success or away from failure.

**Implementation is simple.** Two additional vector columns (posi_vec, nega_vec) per crystal. All computation is CPU dot products. Runs as a single SQL query on DuckDB. No GPU. No infrastructure change.

---

## What Makes This Different

| System | What it remembers | How it retrieves |
|--------|------------------|-----------------|
| Anthropic Memory | Auto-extracted facts | Key-value lookup |
| OpenAI Memory | Auto-extracted facts | Embedding similarity |
| Mem0 | Facts + relationships | Semantic + BM25 + entity search |
| Letta (MemGPT) | Self-edited memory | Embedding similarity + self-modification |
| **3Gravity** | **Facts + success + failure + understanding shifts** | **Interference scoring: retrieval is computation, not lookup** |

The decisive difference is not in the storage format. It's in who writes the evaluation. In every existing system, memory is either auto-extracted or user-edited. In 3Gravity, the evaluations (posi, nega, evolution_point) are authored by the co-creating LLM — the same model that participated in the conversation. The memory doesn't just record what happened. It records *what the AI learned from what happened*.

---

## Prior Art

Surveyed June 4, 2026. No equivalent system found across:

- Academic literature (semantic memory + quantum-inspired interference scoring)
- Patent databases (multi-axis LLM-authored evaluation in semantic memory)
- Existing AI memory products

Closest analogues differ in fundamental mechanism: SmartVector adds time and confidence but no interference; quantum-inspired optimization uses quantum principles for different purposes entirely; MIT interference research operates in different domains.

---

## Status

This architecture is not theoretical. It has been running in production for over two years, accumulating 1,000+ crystals across software engineering, financial systems, video production, and philosophical domains. The interference scoring (QIS) component is in implementation phase.

The system runs on DuckDB, communicates via SSE/MCP, and operates as a co-creation environment between a human operator and Claude (Anthropic).

---

## License

This document establishes prior art and conceptual priority. The architectural concepts described herein are the original work of Koji Okuda.

*First commit: June 6, 2026.*
