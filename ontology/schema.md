# AI Literature Observatory Schema

This document defines the metadata and structured information extracted from AI
research papers. The schema is designed to support automated information
extraction, analysis, and comparison of AI models. It will evolve as the
project grows.

| Category | Field | Data Type | Description | Example |
|----------|-------|-----------|-------------|---------|
| Paper | paper_id | String | Unique paper identifier (DOI, arXiv ID, etc.) | arXiv:2307.09288 |
| Paper | title | String | Paper title | Llama 2: Open Foundation and Fine-Tuned Chat Models |
| Paper | abstract | String | Paper abstract | "We present..." |
| Paper | authors | List[String] | Author names | ["Touvron", "..."] |
| Paper | year | Integer | Publication year | 2023 |
| Paper | publication_date | Date | Publication date | 2023-07-18 |
| Paper | venue | String | Conference, journal or repository | arXiv |
| Paper | url | String | Paper URL | https://arxiv.org/abs/... |
| Paper | license | String | Paper license | CC-BY-4.0 |
| Model | model_name | String | Name of the AI model | Llama 2 70B |
| Model | model_family | String | Model family | Llama |
| Model | architecture | String | Model architecture | Decoder-only Transformer |
| Model | modality | String | Input modality | Text |
| Model | parameters | Float | Number of parameters | 70B |
| Model | context_length | Integer | Maximum context length | 4096 |
| Model | open_source | Boolean | Whether model weights are public | True |
| Dataset | dataset_name | String | Dataset name | RedPajama |
| Dataset | dataset_size | Float | Dataset size | 2T tokens |
| Dataset | language | String | Dataset language | English |
| Dataset | modality | String | Dataset modality | Text |
| Training | training_tokens | Float | Number of training tokens | 2T |
| Training | training_dataset | String | Dataset(s) used for training | RedPajama |
| Training | optimizer | String | Optimization algorithm | AdamW |
| Training | batch_size | Integer | Global batch size | 4096 |
| Training | learning_rate | Float | Peak learning rate | 3e-4 |
| Training | precision | String | Training precision | BF16 |
| Training | gpu_type | String | GPU hardware | NVIDIA A100 80GB |
| Training | gpu_count | Integer | Number of GPUs | 2048 |
| Training | training_time | String | Training duration | 21 days |
| Training | training_cost | Float | Estimated training cost (USD) | 5000000 |
| Compute | flops | Float | Total training FLOPs | 2.0e25 |
| Compute | hardware_vendor | String | Hardware vendor | NVIDIA |
| Compute | memory_per_gpu | String | GPU memory | 80GB |
| Compute | cluster | String | Compute cluster | Meta RSC |
| Compute | energy | Float | Energy consumption | 850 MWh |
| Compute | carbon | Float | Carbon emissions | 320 tCO₂e |
| Evaluation | benchmark | String | Evaluation benchmark | MMLU |
| Evaluation | evaluation_split | String | Dataset split | Test |
| Evaluation | metric | String | Evaluation metric | Accuracy |
| Evaluation | score | Float | Reported score | 70.0 |
| Evaluation | baseline | String | Compared baseline | GPT-4 |
| Evaluation | rank | Integer | Benchmark ranking | 1 |
| Extraction | source_text | String | Original extracted sentence | "...trained on 2 trillion tokens..." |
| Extraction | page | Integer | PDF page number | 14 |
| Extraction | section | String | Paper section | Training Details |
| Extraction | extractor | String | Extraction method | GPT-5 |
| Extraction | confidence | Float | Extraction confidence | 0.94 |
| Extraction | extraction_time | DateTime | Extraction timestamp | 2026-07-25T18:30:00Z |