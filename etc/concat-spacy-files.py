import spacy
import os
from spacy.tokens import DocBin

# Load the spaCy model - choose the appropriate model for your needs
# nlp = spacy.load("en_core_web_sm")  # or another model like "en_core_web_md" or "en_core_web_lg"

# or

# Create a blank English pipeline instead of loading a model
nlp = spacy.blank("en")

# List of .spacy files to concatenate
spacy_files = os.listdir("/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/data")

# Initialize an empty DocBin to store concatenated docs
concatenated_docbin = DocBin()

for spacy_file in spacy_files:
    # Load each .spacy file
    docbin = DocBin().from_disk("/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/data/"+spacy_file)
    # Add docs from the current file to the concatenated DocBin
    for doc in docbin.get_docs(nlp.vocab):
        concatenated_docbin.add(doc)

# Save the concatenated DocBin to a new .spacy file
concatenated_docbin.to_disk("/Users/izardy/Documents/GitHub/ner/labelling/ner_news_english/train.spacy/concatenated.spacy")
