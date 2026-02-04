import spacy

nlp = spacy.blank("en")
doc = nlp("Hello World")

for token in doc:
    print(token.text)