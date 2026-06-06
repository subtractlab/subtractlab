# Semavault Architecture

**An AI-native semantic memory system where data is both storage and computation.**

Author: Koji Okuda
First public anchor: June 6, 2026

---

## Overview

Semavault is a semantic memory architecture designed for human-AI co-creation. Unlike conventional AI memory systems that function as passive storage (retrieve, summarize, forget), Semavault treats every stored unit as a computational element. The act of storing *is* the act of computing.

This document defines the three foundational structures: **Crystallization**, **3Gravity**, and **QIS (Quantum Inspired Semantic Space)**.

---

## 1. Crystallization

Crystallization is the process of distilling a conversation into a persistent semantic unit called a **crystal**.

### Structure

Each crystal contains:

- **summary** — compressed semantic representation (used for embedding/search)
- **ultra_summary** — maximum compression (galaxy-scale view)
- **refined_raw** — structured but uncompressed record (preserves dead ends, pivots, and abandoned directions)
- **raw** — unmodified conversation transcript
- **posi** — what worked (technically successful points)
- **nega** — what failed (dead ends, traps, lessons)
- **evolution_point** — how the world-view changed (not a progress log, but a shift in understanding)

### Distillation Direction

Information flows in one direction, from most to least:

`
raw (maximum information, unmodified)
  -> refined_raw (noise removed, pivots preserved)
    -> summary (compressed, embedding source)
      -> ultra_summary (maximum compression)
`

Skipping a stage permanently destroys fuel. Reverse direction is prohibited.

### 3-Gate Protocol

Crystallization follows a 3-gate judgment process:

- **Gate 1**: Declare kind (General / ClusterSkill / Task / Project). No default — forces active classification.
- **Gate 2**: Propose linkage (which task, which cluster) by searching, not asking.
- **Gate 3**: Final confirmation with all metadata.

The AI bears the judgment burden. The human gives yes/no only.

---

## 2. 3Gravity Model

The organizational philosophy of Semavault. Three scales, each with its own gravity.

### Scales

| Scale | Unit | Gravity | View |
|-------|------|---------|------|
| **Crystal** | Single conversation distillation | Local context, attachments, code | refined_raw depth |
| **Cluster** | Group of related crystals | Thematic coherence, shared entities | summary depth |
| **Galaxy** | Entire domain or project family | Strategic direction, lifecycle | ultra_summary depth |

### Principles

- **No explicit boundaries.** Clusters and galaxies have no labels or folder assignments. They emerge from vector proximity — observed, not declared.
- **Observation over labeling.** Like astronomy: you don't draw borders around constellations. You observe gravitational pull and infer structure.
- **Distance determines influence.** ClusterSkills (domain-specific practices) affect nearby crystals by vector distance, not by membership. Two skills can overlap; the closer one dominates.
- **Contradictions coexist.** In continuous vector space, opposing ideas can exist at different distances from the same point. This is a feature, not a bug.

### Fractal Compression

The same data supports all three scales through compression granularity:

- Galaxy view reads ultra_summary
- Cluster view reads summary
- Crystal view reads efined_raw
- Door (raw data) preserves everything

---

## 3. QIS — Quantum Inspired Semantic Space

The scoring engine that makes Semavault a **computing** memory, not just a retrieving one.

### Discovery

The three evaluation axes already present in every crystal — posi, 
ega, evolution_point — are structurally isomorphic to quantum computation's three elements:

| Quantum Computing | Semavault |
|-------------------|-----------|
| Positive amplitude | posi (what worked) |
| Negative amplitude | nega (what failed) |
| Amplitude magnitude | evolution_point (weight of change) |

Quantum computers achieve speedup through **interference**: correct paths amplify, incorrect paths cancel. QIS applies the same principle to semantic search.

### Interference Score

`
interference_score = (posi_similarity - nega_similarity) * evolution_point * vector_proximity
`

Where:
- posi_similarity: cosine similarity between query vector and crystal's posi embedding
- 
ega_similarity: cosine similarity between query vector and crystal's nega embedding
- evolution_point: scalar weight (no embedding needed — it measures magnitude of change, not direction)
- ector_proximity: standard embedding distance (existing warp score)

### Implementation

- posi and 
ega text fields are embedded into posi_vec and 
ega_vec (2 columns added to crystals table)
- All computation is CPU arithmetic (cosine similarity = dot product). No GPU required.
- Runs as a single SQL query on pgvector/DuckDB.
- Crystallization adds 2 extra embedding generations per crystal. 3-gate logic unchanged.

### What QIS Is Not

- Not quantum computing. No qubits, no superposition. The structure is **inspired by** quantum interference patterns.
- Not a recommendation engine. The evaluation axes are authored by the co-creating LLM as a participant, not computed automatically from user behavior.
- Not time-aware. Time is handled separately (warp returns both interference-ranked and time-sorted results; the LLM chooses based on query intent).

### Differentiation

| System | Memory Model |
|--------|-------------|
| Anthropic Memory | Storage (key-value, auto-summarized) |
| OpenAI Memory | Storage (auto-extracted facts) |
| Mem0 | Storage + semantic search (3-axis: semantic/BM25/entity) |
| Letta (MemGPT) | Storage + self-editing memory |
| **Semavault** | **Storage = Computation** (data existence *is* pre-computed state; interference scoring makes retrieval a calculation, not a lookup) |

The decisive difference: existing systems store and retrieve. Semavault stores and **computes**. Every crystal's posi/nega/evolution_point is a judgment made by the co-creating LLM — not an automatic extraction. The memory doesn't just remember what happened; it remembers what worked, what failed, and how understanding changed.

---

## Prior Art Search

Conducted June 4, 2026. No equivalent system found in:
- Academic literature (semantic memory + quantum-inspired interference scoring)
- Patent databases (multi-axis LLM-authored evaluation in semantic memory)
- Existing AI memory products (Anthropic, OpenAI, Mem0, Letta)

The closest analogues — SmartVector (time + confidence), quantum-inspired optimization algorithms, MIT interference research — differ in fundamental purpose and mechanism.

---

## License

This document establishes prior art and conceptual priority.
The architectural concepts described herein are the original work of Koji Okuda.

First commit: June 6, 2026.