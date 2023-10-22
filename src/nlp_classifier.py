#import
import spacy
#load the model
nlp = spacy.load("en_core_web_md")
text = "+(a,b)"
doc = nlp(text)
x = {}
x1 = []
for token in doc:
    # print(token.text, token.vector)
    x[token.text] = token.vector
    x1.append(token.vector)

# print(f"x: {len(x1)}")
y = [0,1,2,1,2,1]

#classifier
from sklearn.svm import SVC

classifier = SVC(kernel = "rbf")
classifier.fit(x1,y)

text = "+( a,b)"
doc = nlp(text)
for token in doc:
    print(token.text,classifier.predict([token.vector]))
