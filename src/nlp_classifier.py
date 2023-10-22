#import
import spacy
#load the model
nlp = spacy.load("en_core_web_md")
text = "+(a,b)"
doc = nlp(text)
x = []
for token in doc:
    x.append(token.vector)

y = ["operator","bracket","variable","comma","variable","bracket"]
# 0-operator, 1-variable, 2-bracket, 3-comma
# y = [0,2,1,3,1,2]

#classifier
from sklearn.svm import SVC

classifier = SVC(kernel = "rbf")
classifier.fit(x,y)

text = "+( c, b )"
doc = nlp(text)
for token in doc:
    print(token.text,classifier.predict([token.vector]))
