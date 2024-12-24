| Feature | Description |
| --- | --- |
| **Name** | `en_spacy_ner_finetuned_news_article` |
| **Version** | `0.0.0` |
| **spaCy** | `>=3.8.3,<3.9.0` |
| **Default Pipeline** | `transformer`, `ner` |
| **Components** | `transformer`, `ner` |
| **Vectors** | 0 keys, 0 unique vectors (0 dimensions) |
| **Sources** | n/a |
| **License** | n/a |
| **Author** | [Izardy]() |

### Label Scheme

<details>

<summary>View label scheme (15 labels for 1 components)</summary>

| Component | Labels |
| --- | --- |
| **`ner`** | `EVENT`, `FAC`, `GPE`, `LAW`, `LOC`, `MONEY`, `NORP`, `ORDINAL`, `ORG`, `PERCENT`, `PERSON`, `PRODUCT`, `QUANTITY`, `TIME`, `WORK_OF_ART` |

</details>

### Accuracy

| Type | Score |
| --- | --- |
| `ENTS_F` | 98.23 |
| `ENTS_P` | 98.40 |
| `ENTS_R` | 98.06 |
| `TRANSFORMER_LOSS` | 32370.35 |
| `NER_LOSS` | 49704.80 |