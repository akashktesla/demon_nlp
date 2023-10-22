import spacy
from sklearn.svm import SVC
import pandas as pd
from data_builder import build_data
from joblib import dump, load

nlp = spacy.load("en_core_web_md")
def main():
    #return classifier by training the model
    # clf = train_clf_model()
    #save data
    # dump(clf,'models/math_classifier.joblib')

    clf = load('models/math_classifier.joblib')
    test_clf_model(clf)


#to train the classifier
def train_clf_model():
    #build data builds the data from the csv gets the word vector and returns x,y
    x,y = build_data("dataset/math_dataset.csv")
    #classifier with rbf kernel
    clf = SVC(kernel = "rbf")
    #training
    clf.fit(x,y)
    return clf

def test_clf_model(clf):
    text = "+( c, b )"
    doc = nlp(text)
    for token in doc:
        print(token.text,clf.predict([token.vector]))

if __name__ =="__main__":
    main()
