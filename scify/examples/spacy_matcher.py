from spacy.matcher import Matcher
import spacy


nlp = spacy.load("en_core_web_sm")
doc = nlp("This is a really nice, green apple. One apple a day ...!")
matcher = Matcher(nlp.vocab)

pattern = [{'ORTH': 'is'}]
for i in range(0,5): #aribtrary number of wild cards in between
    pattern.append({"OP": "?"}) 
pattern.append({"ORTH": "apple"})

matcher.add('test', None, pattern)
spans = [doc[start:end] for match_id, start, end in matcher(doc)]
for span in spans:
    print(spans) #[is a really nice, green apple]
