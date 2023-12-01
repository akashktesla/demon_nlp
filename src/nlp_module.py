import spacy
import numpy as np
from spacy import displacy

def main():
    nlp = spacy.load("en_core_web_trf")
    text = "Akash is a god because Akash is Akash"
    # text = "Your input text goes here."
    doc = nlp(text)
    graph = to_graph(text,nlp)
    
    # Generate the dependency graph
    
    # options = {"compact": True, "color": "blue", "bg": "white", "font": "Source Sans Pro"}
    # displacy.serve(doc, style="dep", options=options)


class Node():
    def __init__(self):
        pass

def to_graph(text,nlp):
    doc = nlp(text) 
    token_map = {}
    node_list = []
    node_map = {}
    token_node_map = {}
    node_id = 1
    #initializing node
    for token in doc:
        node = Node()
        node.id = node_id
        node.text = token.text
        token_node_map[token] = node
        node_map[node_id] = node
        node_id+=1

    for token in doc:
        head_node = token_node_map[token.head]
        node = token_node_map[token]
        try:
            head_node.tail.append((node.id,token.dep_)) 
        except:
            node.tail = [(node.id,token.dep_)]

    print(f"token_map: {token_map}")
    print(f"token_node_map: {token_node_map}")
    for i in node_map:
        node = node_map[i]
        try:
            print(i,node.text,node.id,node.tail)
        except:
            pass



if __name__ == "__main__": 
    main()

