# AI Literature Observatory Relations

## Purpose

This document defines the semantic relationships between the entities in the AI
Literature Observatory ontology.

While `schema.md` specifies the attributes of each entity, this document
describes how those entities are connected.

The relationships defined here will later guide:

- Information extraction
- Database design
- Knowledge graph construction
- Search and analytics

---

# Entity Overview

The observatory models the following primary entities.

```
Paper
│
├── Model
├── Dataset
├── Training
├── Compute
└── Evaluation
```

Each entity contains its own attributes defined in `schema.md`.

---

# Entity Relationships

## Paper

A research paper is the central entity of the system.

A paper may:

- describe one or more models
- use one or more datasets
- report one or more evaluations
- contain one or more training configurations
- report compute requirements

```
Paper
│
├── describes ─────────► Model
├── uses ──────────────► Dataset
├── contains ──────────► Training
├── reports ───────────► Evaluation
└── reports ───────────► Compute
```

---

## Model

A model represents an AI system proposed or evaluated by a paper.

A model:

- is described by a paper
- is trained using one or more datasets
- has one training configuration
- has one compute configuration
- is evaluated using one or more benchmarks

```
Model
│
├── trained_on ────────► Dataset
├── trained_with ──────► Training
├── requires ──────────► Compute
└── evaluated_by ──────► Evaluation
```

---

## Dataset

Datasets provide the training or evaluation data.

A dataset may:

- train many models
- evaluate many models

```
Dataset
│
├── trains ───────────► Model
└── evaluates ────────► Model
```

---

## Training

Training describes how a model was trained.

Training includes:

- optimizer
- learning rate
- batch size
- precision
- training tokens
- training time

Training belongs to exactly one model.

```
Training
│
└── belongs_to ───────► Model
```

---

## Compute

Compute represents the hardware resources used during training.

Compute includes:

- GPU type
- GPU count
- FLOPs
- energy
- carbon emissions

Compute belongs to one training configuration.

```
Compute
│
└── supports ─────────► Training
```

---

## Evaluation

Evaluation stores benchmark results.

Each evaluation records:

- benchmark
- metric
- score

One model may have many evaluations.

```
Evaluation
│
├── evaluates ────────► Model
└── uses ─────────────► Dataset
```

---

# Relationship Cardinality

The following table summarizes how entities are connected.

| Entity A | Relationship | Entity B | Cardinality |
|-----------|--------------|-----------|-------------|
| Paper | describes | Model | One-to-Many |
| Paper | uses | Dataset | Many-to-Many |
| Paper | contains | Training | One-to-Many |
| Paper | reports | Evaluation | One-to-Many |
| Paper | reports | Compute | One-to-Many |
| Model | trained_on | Dataset | Many-to-Many |
| Model | trained_with | Training | One-to-One |
| Model | requires | Compute | One-to-One |
| Model | evaluated_by | Evaluation | One-to-Many |
| Evaluation | uses | Dataset | Many-to-One |
| Training | belongs_to | Model | One-to-One |
| Compute | supports | Training | One-to-One |

---

# Knowledge Graph Representation

The relationships can be represented as a graph.

```
                    +-------------+
                    |    Paper    |
                    +-------------+
                     /     |      \
                    /      |       \
                   /       |        \
                  ▼        ▼         ▼
            +--------+ +---------+ +-----------+
            | Model  | | Dataset | | Training |
            +--------+ +---------+ +-----------+
                |          ▲            |
                |          |            |
                ▼          |            ▼
          +------------+   |      +-----------+
          | Evaluation |---+----->| Compute   |
          +------------+          +-----------+
```

---

# Future Extensions

The ontology is intentionally designed to be extensible.

Future entities may include:

- Author
- Institution
- Organization
- Research Area
- License
- Citation
- Repository
- Code Release
- Model Checkpoint
- Fine-tuning Dataset
- Safety Evaluation
- Human Evaluation
- Inference Benchmark
- Deployment Environment

These entities can be connected without modifying the existing architecture.

---

# Design Principles

The ontology follows several principles.

1. **Modularity**

Each entity represents a single concept.

---

2. **Extensibility**

New entities and relationships can be added without redesigning the system.

---

3. **Traceability**

Every extracted value should be traceable back to its source text in the paper.

---

4. **Normalization**

Information should be represented once and referenced through relationships whenever possible.

---

5. **Research-Oriented**

The ontology is designed to support literature analysis, benchmarking, trend discovery, and automated knowledge extraction rather than simple document storage.