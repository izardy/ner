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
### spaCY Training Data Preparation
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
### spaCY Training Configuration


## Environment Setup
## Miniconda Installation
### Create Environment
#### Python 3.10
- Create environment with Python 3.10:
  - `conda create --name myenv python=3.10`
  - `conda activate myenv`
  - `pip install -r requirements.txt`

