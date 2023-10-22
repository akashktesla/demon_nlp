import spacy
import ast
from sklearn.svm import SVC
import pandas as pd
nlp = spacy.load("en_core_web_md")

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
    return x,y



#-----saving------
#creating a dataframe
# data = {'x':x, 'y': y}
# df = pd.DataFrame(data)
# df.to_csv('dataset/math_dataset_proc.csv')




