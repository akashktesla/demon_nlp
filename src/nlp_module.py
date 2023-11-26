import spacy
import numpy as np
from spacy import displacy

def main():
    nlp = spacy.load("en_core_web_trf")
    text = "Running swiftly through the forest, the wind whispered secrets, and the leaves danced with joy. The sun sets over the horizon, casting a warm glow on the tranquil sea."

    # text = "Your input text goes here."
    doc = nlp(text)
    graph = to_graph(text,nlp)
    
    # Generate the dependency graph
    
    options = {"compact": True, "color": "blue", "bg": "white", "font": "Source Sans Pro"}
    displacy.serve(doc, style="dep", options=options)



def to_graph(text,nlp):
    doc = nlp(text) 
    for token in doc:
        print(f"Token: {token.text}, Dependency: {token.dep_}, Head: {token.head.text}")

if __name__ == "__main__": main()

