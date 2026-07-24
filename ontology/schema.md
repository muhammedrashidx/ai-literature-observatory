# AI Literature Observatory Schema

## Purpose

This document defines the metadata and information extracted from AI research papers.
The schema will evolve as the project grows.

| Category | Field | Data Type | Description | Example |
|----------|-------|-----------|-------------|---------|
| Paper | paper_id | String | Unique identifier (DOI, arXiv ID, etc.) | arXiv:2307.09288 |
| Paper | title | String | Paper title | Llama 2: Open Foundation and Fine-Tuned Chat Models |
| Paper | year | Integer | Publication year | 2023 |
| Paper | venue | String | Conference, journal or repository | arXiv |
| Paper | authors | List[String] | Author names | ["Touvron", "..."] |
| Model | model_name | String | Name of the AI model | Llama 2 70B |
| Model | model_family | String | Model family | Llama |
| Model | parameters | Float | Number of parameters | 70B |
| Training | training_tokens | Float | Number of training tokens | 2T |
| Training | training_dataset | String | Dataset(s) used for training | RedPajama |
| Training | gpu_type | String | GPU hardware | A100 80GB |
| Training | gpu_count | Integer | Number of GPUs | 2048 |
| Training | training_time | String | Training duration | 21 days |
| Compute | flops | Float | Total training FLOPs | 2.0e25 |
| Compute | energy | Float | Energy consumption | 850 MWh |
| Compute | carbon | Float | Carbon emissions | 320 tCO₂e |
| Evaluation | benchmark | String | Evaluation benchmark | MMLU |
| Evaluation | metric | String | Metric name | Accuracy |
| Evaluation | score | Float | Reported score | 70.0 |
| Extraction | source_text | String | Original extracted sentence | "...trained on 2 trillion tokens..." |
| Extraction | confidence | Float | Extraction confidence | 0.94 |