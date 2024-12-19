# spaCY's NER Customized Model Development
## What is spaCy NER ?
spaCy NER (Named Entity Recognition) is a feature of the spaCy library, which is a powerful and efficient tool for natural language processing (NLP) in Python. Named Entity Recognition is a standard NLP task that involves identifying and classifying named entities in text into predefined categories such as persons, organizations, locations, dates, and more.
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
## Environment Setup
## Miniconda Installation
### Create Environment
#### Python 3.10
- Create environment with Python 3.10:
  - `conda create --name myenv python=3.10`
  - `conda activate myenv`
  - `pip install -r requirements.txt`

