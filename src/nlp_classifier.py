##import
#import spacy
##load the model
#nlp = spacy.load("en_core_web_md")
#text = "+(a,b)"

#doc = nlp(text)

#for token in doc:
#    print(token.text, token.vector)

from sklearn.svm import SVC

classifier = SVC(kernel = "linear")
print(classifier)
