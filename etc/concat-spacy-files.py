import spacy
from spacy.tokens import DocBin

# List of .spacy files to concatenate
spacy_files = ["file1.spacy", "file2.spacy", "file3.spacy"]

# Initialize an empty DocBin to store concatenated docs
concatenated_docbin = DocBin()

for spacy_file in spacy_files:
    # Load each .spacy file
    docbin = DocBin().from_disk(spacy_file)
    # Add docs from the current file to the concatenated DocBin
    for doc in docbin.get_docs(nlp.vocab):
        concatenated_docbin.add(doc)

# Save the concatenated DocBin to a new .spacy file
concatenated_docbin.to_disk("concatenated.spacy")