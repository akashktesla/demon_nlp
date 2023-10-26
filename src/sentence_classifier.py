from sentence_transformers import SentenceTransformer
import numpy as np

# Load a pre-trained model, such as "paraphrase-MiniLM-L6-v2"
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Example sentences
sentences = ["I hate you", "coconut", "I love you"]

# Generate sentence embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

# Now you have vector representations for the sentences
for sentence, vector in zip(sentences, embeddings):
    print(f"Sentence: {sentence}")
    print(f"Vector: {vector}")
    print()
