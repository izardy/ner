# spaCY's NER Customized Model Development
## What is spaCy NER ?
- spaCy NER (Named Entity Recognition) is a feature of the spaCy library, which is a powerful and efficient tool for natural language processing (NLP) in Python. Named Entity Recognition is a standard NLP task that involves identifying and classifying named entities in text into predefined categories such as persons, organizations, locations, dates, and more.
### Example Usage (Pre-Trained Model):
```
import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Print the entities
for ent in doc.ents:
    print(ent.text, ent.label_)
```
### Example Usage (Custom Model):
```
import spacy

# Load a new spacy model for first time 
# nlp = spacy.blank("en")

# Load the custom model if available 
nlp = spacy.load("/path/to/your/spacy/model")

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

# Print the entities
for ent in doc.ents:
    print(ent.text, ent.label_)
```
## spaCY Training Data Preparation
### Data Annotation
- spaCY training data must be labelled . The term label here referring to the entity we wish to extract from the texts. The origin of this texts could be from many sources i.e. news articles, transcripts, logs etc whereby the compilations of these texts come in various format such as parquet, json or csv. These text could contains numbers as entities depands on the user's requirement. Example of entities includes:-

> - <sup>PERSON:      People, including fictional.</sup>
> - <sup>NORP:        Nationalities or religious or political groups.</sup>
> - <sup>FAC:         Buildings, airports, highways, bridges, etc.</sup>
> - <sup>ORG:         Companies, agencies, institutions, etc.</sup>
> - <sup>GPE:         Countries, cities, states.</sup>
> - <sup>LOC:         Non-GPE locations, mountain ranges, bodies of water.</sup>
> - <sup>PRODUCT:     Objects, vehicles, foods, etc. (Not services.)</sup>
> - <sup>EVENT:       Named hurricanes, battles, wars, sports events, etc.</sup>
> - <sup>WORK_OF_ART: Titles of books, songs, etc.</sup>
> - <sup>LAW:         Named documents made into laws.</sup>
> - <sup>LANGUAGE:    Any named language.</sup>
> - <sup>DATE:        Absolute or relative dates or periods.</sup>
> - <sup>TIME:        Times smaller than a day.</sup>
> - <sup>PERCENT:     Percentage, including ”%“.</sup>
> - <sup>MONEY:       Monetary values, including unit.</sup>
> - <sup>QUANTITY:    Measurements, as of weight or distance.</sup>
> - <sup>ORDINAL:     “first”, “second”, etc.</sup>
> - <sup>CARDINAL:    Numerals that do not fall under another type.</sup>

- Entities must be defined for data labelling purpose. Code example for defining entities:-
```
labels=["GPE","PERSON","ORG","FAC","MONEY","NORP","LOC","PRODUCT","EVENT","PERCENT","WORK_OF_ART","TIME","ORDINAL","CARDINAL","QUANTITY","LAW"]
```
- Using Jupyter notebook, paste the following code for data annotation
```
import spacy
from spacy import displacy
import spacy_annotator as spa
import pandas as pd
import numpy as np

nlp = spacy.blank("en") # load a new spacy model for first time 
# nlp = spacy.load("output/model-best") # load custom model after first time train / or if available

# prepare train data
import spacy_annotator as spa

train_data=pd.DataFrame({
    "text":pd.read_parquet('./your/data/path').loc[i:j]['column_to_retrieve_the_entities'].tolist()}) # i, j represent integer to chunk your data

annotator=spa.Annotator(labels=["GPE","PERSON","ORG","FAC","MONEY","NORP","LOC","PRODUCT","EVENT","PERCENT","WORK_OF_ART","TIME","ORDINAL","CARDINAL","QUANTITY","LAW"],model=nlp) #annotate train data

df_labels=annotator.annotate(df=train_data,col_text="text",shuffle=False)

spacy_annotations = annotator.to_spacy(df_labels,"./train/train_i_j.spacy") # "train" is the folder where all labelled data portion save

```
## NER Model Training
### spaCY Training Configuration
- As per spaCY documentations
> Config files used for training should always be complete and not contain any hidden defaults or missing values, so this command helps you create your final training config. In order to find the available settings and defaults, all functions referenced in the config will be created, and their signatures are used to find the defaults.
>
- base_config.cfg (cpu)
```
# This is an auto-generated partial config. To use it with 'spacy train'
# you can run spacy init fill-config to auto-fill all default settings:
# python -m spacy init fill-config ./base_config.cfg ./config.cfg
[paths]
train = null
dev = null
vectors = null
[system]
gpu_allocator = null

[nlp]
lang = "en"
pipeline = ["tok2vec","ner"]
batch_size = 1000

[components]

[components.tok2vec]
factory = "tok2vec"

[components.tok2vec.model]
@architectures = "spacy.Tok2Vec.v2"

[components.tok2vec.model.embed]
@architectures = "spacy.MultiHashEmbed.v2"
width = ${components.tok2vec.model.encode.width}
attrs = ["NORM", "PREFIX", "SUFFIX", "SHAPE"]
rows = [5000, 1000, 2500, 2500]
include_static_vectors = false

[components.tok2vec.model.encode]
@architectures = "spacy.MaxoutWindowEncoder.v2"
width = 96
depth = 4
window_size = 1
maxout_pieces = 3

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
state_type = "ner"
extra_state_tokens = false
hidden_width = 64
maxout_pieces = 2
use_upper = true
nO = null

[components.ner.model.tok2vec]
@architectures = "spacy.Tok2VecListener.v1"
width = ${components.tok2vec.model.encode.width}

[corpora]

[corpora.train]
@readers = "spacy.Corpus.v1"
path = ${paths.train}
max_length = 0

[corpora.dev]
@readers = "spacy.Corpus.v1"
path = ${paths.dev}
max_length = 0

[training]
dev_corpus = "corpora.dev"
train_corpus = "corpora.train"

[training.optimizer]
@optimizers = "Adam.v1"

[training.batcher]
@batchers = "spacy.batch_by_words.v1"
discard_oversize = false
tolerance = 0.2

[training.batcher.size]
@schedules = "compounding.v1"
start = 100
stop = 1000
compound = 1.001

[initialize]
vectors = ${paths.vectors}
```
- base_config.cfg (gpu)
```
# This is an auto-generated partial config. To use it with 'spacy train'
# you can run spacy init fill-config to auto-fill all default settings:
# python -m spacy init fill-config ./base_config.cfg ./config.cfg
[paths]
train = null
dev = null
vectors = null
[system]
gpu_allocator = "pytorch"

[nlp]
lang = "en"
pipeline = ["transformer","ner"]
batch_size = 128

[components]

[components.transformer]
factory = "transformer"

[components.transformer.model]
@architectures = "spacy-transformers.TransformerModel.v3"
name = "roberta-base"
tokenizer_config = {"use_fast": true}

[components.transformer.model.get_spans]
@span_getters = "spacy-transformers.strided_spans.v1"
window = 128
stride = 96

[components.ner]
factory = "ner"

[components.ner.model]
@architectures = "spacy.TransitionBasedParser.v2"
state_type = "ner"
extra_state_tokens = false
hidden_width = 64
maxout_pieces = 2
use_upper = false
nO = null

[components.ner.model.tok2vec]
@architectures = "spacy-transformers.TransformerListener.v1"
grad_factor = 1.0

[components.ner.model.tok2vec.pooling]
@layers = "reduce_mean.v1"

[corpora]

[corpora.train]
@readers = "spacy.Corpus.v1"
path = ${paths.train}
max_length = 0

[corpora.dev]
@readers = "spacy.Corpus.v1"
path = ${paths.dev}
max_length = 0

[training]
accumulate_gradient = 3
dev_corpus = "corpora.dev"
train_corpus = "corpora.train"

[training.optimizer]
@optimizers = "Adam.v1"

[training.optimizer.learn_rate]
@schedules = "warmup_linear.v1"
warmup_steps = 250
total_steps = 20000
initial_rate = 5e-5

[training.batcher]
@batchers = "spacy.batch_by_padded.v1"
discard_oversize = true
size = 2000
buffer = 256

[initialize]
vectors = ${paths.vectors}
```
- As per spaCY documentation
> After you’ve saved the starter config to a file base_config.cfg, you can use the init fill-config command to fill in the remaining defaults. Training configs should always be complete and without hidden defaults, to keep your experiments reproducible.
```
python -m spacy init fill-config base_config.cfg config.cfg
```
### spaCY Training init
- Using the both labelled data (train folder) and cofig.cfg file, ner model training initiated as code below
```
python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev --gpu-id 0 # if using gpu to train
# python -m spacy train config.cfg --output ./output --paths.train ./train --paths.dev ./dev # if using cpu to train
```

#### Command Breakdown
- ```python -m spacy train```: This runs the spacy module's train command, which is used to train a spaCy model.

- ```config.cfg```: This is the configuration file that contains all the settings and parameters for training the model. It includes details like the pipeline components, training data paths, and hyperparameters.

- ```--output ./output```: This specifies the directory where the trained model and other output files will be saved. In this case, it's the ./output directory.

- ```--paths.train ./train```: This sets the path to the training data. The training data is located in the ./train directory.

- ```--paths.dev ./dev```: This sets the path to the development (validation) data. The development data is located in the ./dev directory.

- ```--gpu-id 0```: This specifies the GPU to use for training. 0 indicates the first GPU. If you want to use the CPU instead, you can omit this option.


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

# Upload the entire model directory ,considering code run within the same folder where folder_path contain
upload_folder(
    folder_path="wheel folder",
    repo_id="huggingface_id/repo_name",
    repo_type="model"
)
```

## Environment Setup
### Pytorch Installation
#### MacOS (Apple Silicon)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install miniforge
```
#### Windows
```
# Download the latest Miniconda installer
Invoke-WebRequest -Uri "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -OutFile "Miniconda3-latest-Windows-x86_64.exe"

# Silent installation with recommended options
Start-Process -Wait -FilePath ".\Miniconda3-latest-Windows-x86_64.exe" -ArgumentList "/S /RegisterPython=1 /AddToPath=1"

# Initialize conda for PowerShell
conda init powershell

# Close and reopen PowerShell for changes to take effect
```
#### Linux
```
# Download the latest Miniconda installer
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

# Create directory for miniconda
mkdir -p ~/miniconda3

# Run the installer
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# Remove the installer
rm -rf ~/miniconda3/miniconda.sh

# Initialize conda for your shell (both bash and zsh)
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh

# For bash
source ~/.bashrc

# For zsh
source ~/.zshrc
```

### Miniconda Installation
#### Create Environment
##### Python 3.10
- Create environment with Python 3.10:
  - `conda create --name myenv python=3.10`
  - `conda activate myenv`
  - `pip install -r requirements.txt`
  - `pip install torch torchvision torchaudio`

