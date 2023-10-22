#classifier
from sklearn.svm import SVC
import pandas as pd
import ast


#importing data
df = pd.read_csv("dataset/math_dataset_proc.csv")
x = df['x'].apply(ast.literal_eval).to_numpy()
y = df['y'].to_numpy()

print(x)
print(y)


classifier = SVC(kernel = "rbf")
classifier.fit(x,y)

text = "+( c, b )"
doc = nlp(text)
for token in doc:
    print(token.text,classifier.predict([token.vector]))
