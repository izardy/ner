## Model Overview

### Result

```
=========================== Initializing pipeline ===========================
✔ Initialized pipeline

============================= Training pipeline =============================
ℹ Pipeline: ['transformer', 'ner']
ℹ Initial learn rate: 0.0
E    #       LOSS TRANS...  LOSS NER  ENTS_F  ENTS_P  ENTS_R  SCORE 
---  ------  -------------  --------  ------  ------  ------  ------
  0       0        1027.60   2028.92    0.00    0.00    0.01    0.00
  0     200      225652.63  77443.33   17.55   20.90   15.12    0.18
  0     400       34799.92  12790.88   69.73   69.77   69.69    0.70
  0     600       16755.79   9699.92   74.23   69.75   79.32    0.74
  1     800        5509.15   8061.05   77.48   72.91   82.65    0.77
  1    1000        5524.08   8379.61   78.38   72.42   85.41    0.78
  1    1200        4490.30   7921.10   81.05   77.75   84.65    0.81
  2    1400        4319.48   6579.05   81.78   79.93   83.72    0.82
  2    1600        3331.55   6981.83   80.43   72.27   90.67    0.80
  2    1800        2940.46   6159.03   82.06   75.51   89.86    0.82
  3    2000        2940.73   5604.61   84.07   83.55   84.58    0.84
  3    2200        5573.14   6000.54   85.11   82.78   87.57    0.85
  3    2400        2792.99   5804.08   85.59   83.59   87.69    0.86
...
 22   13600         236.77    340.90   97.73   97.00   98.47    0.98
 22   13800         221.60    333.28   98.20   97.99   98.42    0.98
 ```

#### spaCY Training pipeline
- Descirption of training pipelne output for spaCy NER trainin
  - ```E``` - Epoch number: Shows which training epoch/iteration you're on
  - ```#``` - Step/batch number
  - ```LOSS TRANS``` - Transition Loss: Loss value for the transition component of the model, which helos in learning valid entity transitions
  - ```LOSS NER``` - Named Entity Recognition Loss: The loss value specifically for the NER component, indicating how well the model is learning to identify entities
  - ```ENTS_F``` -  Entities F-Score: The harmonic mean of precision and recall (F1 score) for entity recognition. Range is 0-100, higher is better
  - ```ENTS_P``` -  Entities Precision: The percentage of entities predicted by the model that are correct. Range is 0-100
    > <sup> Precision = (True Positives) / (True Positives + False Positives)
  - ```ENTS_R``` - Entities Recall: The percentage of actual entities that were correctly identified by the model. Range is 0-100
    > <sup> Recall = (True Positives) / (True Positives + False Negatives)
  - ```SCORE``` - Overall Score: The main metric used to evaluate model performance, typically the same as ENTS_F

#### Model Evaluation
- A good model should show:
  - Decreasing loss values over time
  - Increasing F-score, precision, and recall
  - Balanced precision and recall scores

## Model to Huggingface Repository
### Step by step Process:
- Navigate to model's "model-best" directory and edit the meta.json file to set a unique name for the model. For your news English NER model, you might want to name it something like:
```
{
    "name": "en_news_ner_pipeline"
}
```
- Create a wheel file using spaCy's package command:
```
!python -m spacy package "model-best" "./ner-output" --build wheel
```
- Login to Hugging Face Hub. You'll need to have your Hugging Face access token ready:
```
from huggingface_hub import login
login()  # This will prompt for your access token
```
- Create a model card (README.md) with information about the model:
```
model_card = """
---
language: en
license: mit
tags:
- spacy
- ner
- named-entity-recognition
- news
---

# English News NER Model

## Model Description
This is a spaCy NER model trained on English news data to identify named entities.

## Training Data
The model was trained on annotated news articles.

## Entity Labels
[List your entity labels here]

## Usage
```python
import spacy
nlp = spacy.load("your-username/your-model-name")
doc = nlp("Your text here")
for ent in doc.ents:
    print(ent.text, ent.label_)
"""
with open("README.md", "w") as f:
f.write(model_card)
```
- Login into huggingface hub
```
from huggingface_hub import login
login()  # This will prompt for your access token
```
- Crate repository in huggingface where the model to be uploaded
```
# for huggingface new repo
from huggingface_hub import create_repo

create_repo(
    repo_id="your-username/your-model-name",
    repo_type="model",
    private=False  # Set to True if you want a private repository
)
```
- Push the model to the repo
```
#upload to existing huggingface model
from huggingface_hub import upload_folder

# Upload the entire model directory
upload_folder(
    folder_path="en_spacy_ner_finetuned_news_article-0.0.0",
    repo_id="izardy/en_spacy_ner_finetuned_news_article",
    repo_type="model"
)
```
- Check the uploaded model at https://huggingface.co/izardy/en_spacy_ner_finetuned_news_article
