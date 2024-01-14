import torch
import spacy
import numpy as np
from spacy import displacy
from torch_geometric.nn import GCNConv,GraphConv



def main():
    nlp = spacy.load("en_core_web_trf")
    text = "Akash is a god because Akash is Akash"
    # text = "Your input text goes here."
    doc = nlp(text)
    node_feature_matrix, edge_index, edge_feature_matrix = to_graph(text,nlp)
    print(f"node_feture_matrix: {node_feature_matrix}")
    print(f"edge_index: {edge_index}")
    print(f"edge_feature_matrix: {edge_feature_matrix}")
    
    conv1 = GCNConv(1,32)
    conv2 = GCNConv(32,16)
    
    print(conv1(torch.tensor([0.2,0.4,0.3]),torch.tensor([[1,3],[2,1]])))


    
    # Generate the dependency graph
    # options = {"compact": True, "color": "blue", "bg": "white", "font": "Source Sans Pro"}
    # displacy.serve(doc, style="dep", options=options)


class Node():
    def __init__(self):
        # self.tail = []
        pass

def to_graph(text,nlp):
    doc = nlp(text) 
    token_map = {}
    node_list = []
    node_map = {}
    token_node_map = {}
    node_feature_matrix = []
    edge_index = [[],[]]
    edge_feature_matrix = []
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
            node_feature_matrix.append(token.text)
            edge_index[0].append(head_node.id)
            edge_index[1].append(node.id)
            edge_feature_matrix.append([token.dep_])
        except:
            head_node.tail = [(node.id,token.dep_)]
            node_feature_matrix.append(token.text)
            edge_index[0].append(head_node.id)
            edge_index[1].append(node.id)
            edge_feature_matrix.append([token.dep_])

    # print(f"token_map: {token_map}")
    # print(f"token_node_map: {token_node_map}")
    # for i in node_map:
    #     node = node_map[i]
    #     try:
    #         print(f"id:{node.id}, text: {node.text}, tail: {node.tail}")
    #     except:
    #         pass

    return node_feature_matrix,edge_index,edge_feature_matrix



if __name__ == "__main__": 
    main()

