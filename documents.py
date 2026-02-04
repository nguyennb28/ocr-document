import spacy
from spacy_layout import spaCyLayout

nlp = spacy.load("en_core_web_sm")

layout = spaCyLayout(nlp)
doc = layout('./docs/english.pdf')
print(doc.text)