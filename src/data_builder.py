import spacy
import ast
from sklearn.svm import SVC
import pandas as pd
nlp = spacy.load("en_core_web_md")

#load a csv file
df = pd.read_csv("dataset/math_dataset.csv")
x_temp = df["x"].apply(ast.literal_eval).to_numpy()
y_temp = df["y"].to_numpy()

x = []
y = []

print(y_temp)
for i in y_temp:
    y_split = i.split(',')
    for j in y_split:
        y.append(j)

for i in x_temp:
    print(f"i: {i}")
    doc = nlp(i)
    for token in doc:
        print(f"token_text: {token.text}")
        x.append(token.vector)

print(x)
print(f"x: {x}")
print(f"y: {y}")
print(df)

#creating a dataframe
data = {'x':x, 'y': y}
df = pd.DataFrame(data)
df.to_csv('dataset/math_dataset_proc.csv')



classifier = SVC(kernel = "rbf")
classifier.fit(x,y)

text = "-( 21, b )"
doc = nlp(text)
for token in doc:
    print(token.text,classifier.predict([token.vector]))




