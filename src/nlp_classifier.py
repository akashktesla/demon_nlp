import spacy
from sklearn.svm import SVC
import pandas as pd
from joblib import dump, load

nlp = spacy.load("en_core_web_md")

def main():
    #return classifier by training the model
    # clf = train_clf_model()
    #save data
    # dump(clf,'models/math_classifier.joblib')

    test_clf_model('models/math_classifier.joblib')

def build_data(path):
    #load a csv file
    df = pd.read_csv(path)
    x_temp = df["x"].to_numpy()
    y_temp = df["y"].to_numpy()

    x = []
    y = []

    print(y_temp)
    for i in y_temp:
        y_split = i.split(',')
        for j in y_split:
            y.append(j)

    for i in x_temp:
        # print(f"i: {i}")
        doc = nlp(i)
        for token in doc:
            # print(f"token_text: {token.text}")
            #appending the token word vector
            x.append(token.vector)

    # print(x)
    # print(f"x: {x}")
    # print(f"y: {y}")
    # print(df)
    return (x,y)



#-----saving------
#creating a dataframe
# data = {'x':x, 'y': y}
# df = pd.DataFrame(data)
# df.to_csv('dataset/math_dataset_proc.csv')


#to train the classifier
def train_clf_model():
    #build data builds the data from the csv gets the word vector and returns x,y
    x,y = build_data("dataset/math_dataset.csv")
    #classifier with rbf kernel
    clf = SVC(kernel = "rbf")
    #training
    clf.fit(x,y)
    return clf

def test_clf_model(path):
    clf = load(path)
    text = "+( c, b )"
    doc = nlp(text)
    for token in doc:
        print(token.text,clf.predict([token.vector]))

def predict_clf(path, text):
    clf = load(path)
    doc = nlp(text)
    returns = []
    for token in doc:
        # print(token.text,clf.predict([token.vector]))
        returns.append(clf.predict([token.vector])[0])
    return returns




if __name__ =="__main__":
    main()
