import spacy
from spacy_layout import spaCyLayout

nlp = spacy.load("xx_sent_ud_sm")

layout = spaCyLayout(nlp)
doc = layout('./docs/Tieng-Viet-123-Student-book-Demo.pdf')
print(doc.text)