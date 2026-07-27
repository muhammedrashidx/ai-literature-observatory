# AI Literature Observatory Architecture

## Overview

The AI Literature Observatory is a system for automatically extracting structured
knowledge from AI research papers.

The primary objective is to convert unstructured research papers (PDFs) into
structured metadata that can be stored, searched, analyzed, and compared across
thousands of publications.

---

# High-Level Workflow

```
                +------------------+
                |   Research PDF   |
                +------------------+
                          |
                          ▼
                +------------------+
                |   PDF Loader     |
                +------------------+
                          |
                          ▼
                +------------------+
                | Text Extraction  |
                +------------------+
                          |
                          ▼
                +------------------+
                | Section Parser   |
                +------------------+
                          |
                          ▼
                +---------------------------+
                | Information Extraction    |
                +---------------------------+
                          |
                          ▼
                +------------------+
                | Data Validation  |
                +------------------+
                          |
                          ▼
                +------------------+
                | Data Storage     |
                +------------------+
                          |
                          ▼
                +------------------+
                | Search & Analysis|
                +------------------+
```

---

# Pipeline Components

## 1. PDF Loader

### Purpose

Load AI research papers from disk.

### Input

- PDF file

### Output

- PDF document object

### Future Module

```
scripts/pdf_loader.py
```

---

## 2. Text Extraction

### Purpose

Extract plain text from the PDF while preserving reading order.

This stage converts the PDF into raw textual content that later stages can
process.

### Input

- PDF document

### Output

- Plain text

### Future Module

```
scripts/text_extractor.py
```

---

## 3. Section Parser

### Purpose

Identify logical sections within the paper.

Examples:

- Abstract
- Introduction
- Related Work
- Method
- Training Details
- Evaluation
- Conclusion

Splitting the paper into sections improves extraction quality.

### Input

- Plain text

### Output

Structured document

Example

```
{
    "abstract": "...",
    "method": "...",
    "training": "...",
    "evaluation": "..."
}
```

### Future Module

```
scripts/section_parser.py
```

---

## 4. Information Extraction

### Purpose

Extract structured metadata defined by the ontology.

Examples

Paper

- title
- authors
- venue

Model

- model_name
- parameters
- architecture

Training

- dataset
- optimizer
- GPU type
- FLOPs

Evaluation

- benchmark
- metric
- score

Compute

- energy
- carbon emissions

### Input

Structured sections

### Output

Metadata dictionary

Example

```
{
    "paper": {...},
    "model": {...},
    "training": {...},
    "evaluation": {...}
}
```

### Future Module

```
scripts/extractor.py
```

---

## 5. Data Validation

### Purpose

Ensure extracted information is consistent and complete.

Examples

- Parameter count is numeric
- Year is valid
- Confidence score is between 0 and 1
- Required fields exist

### Input

Extracted metadata

### Output

Validated metadata

### Future Module

```
scripts/validator.py
```

---

## 6. Data Storage

### Purpose

Store validated metadata for later analysis.

Early versions

- JSON

Future versions

- SQLite
- PostgreSQL
- Knowledge Graph

### Input

Validated metadata

### Output

Persistent structured data

### Future Module

```
scripts/storage.py
```

---

## 7. Search & Analytics

### Purpose

Provide tools for exploring the collected literature.

Example queries

- Models larger than 70B parameters
- Papers using more than 2T training tokens
- All papers evaluated on MMLU
- GPU usage across model families
- Compare benchmark performance over time

Future visualizations

- Trends over years
- Model family comparisons
- Training compute evolution
- Dataset usage statistics

### Future Module

```
scripts/analytics.py
```

---

# Project Directory Structure

```
ai-literature-observatory/

│
├── data/
│   ├── raw/
│   ├── processed/
│   └── extracted/
│
├── docs/
│   ├── architecture.md
│   └── roadmap.md
│
├── notebooks/
│
├── ontology/
│   ├── schema.md
│   └── relations.md
│
├── scripts/
│   ├── pdf_loader.py
│   ├── text_extractor.py
│   ├── section_parser.py
│   ├── extractor.py
│   ├── validator.py
│   ├── storage.py
│   └── analytics.py
│
├── README.md
└── requirements.txt
```

---

# Development Roadmap

## Phase 1

Project setup

- Repository
- Git workflow
- Ontology
- Architecture

Status

✅ Complete

---

## Phase 2

PDF Processing

Goal

```
PDF

↓

Plain Text
```

Deliverable

Working PDF text extraction.

---

## Phase 3

Metadata Extraction

Goal

```
Plain Text

↓

Structured Metadata
```

Deliverable

Extract paper metadata and AI-specific information.

---

## Phase 4

Validation

Goal

Automatically verify extracted information.

Deliverable

Validated metadata.

---

## Phase 5

Storage

Goal

Store extracted metadata.

Deliverable

JSON and SQLite database.

---

## Phase 6

Analysis

Goal

Explore AI research trends.

Deliverables

- Search interface
- Statistical analysis
- Visualizations
- Benchmark comparisons

---

# Long-Term Vision

The AI Literature Observatory will evolve into a platform capable of automatically
building a structured knowledge base of AI research.

Researchers will be able to search, compare, and analyze thousands of papers
without manually reading every publication.

The architecture is intentionally modular so that each pipeline stage can be
improved independently without affecting the rest of the system.