import spacy
import xx_sent_ud_sm
nlp = spacy.load("xx_sent_ud_sm")
nlp = xx_sent_ud_sm.load()
doc = nlp("This is a sentence about Facebook.")
print([(ent.text, ent.label) for ent in doc.ents])