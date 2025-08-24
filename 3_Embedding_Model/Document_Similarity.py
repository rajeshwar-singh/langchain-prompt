from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

os.environ['HF_HOME'] = 'D:\Rajeshwar\HF_LOCAL_'

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

document = ["Delhi is the capital fof India",
            "Lucknow is the capital of Uttar Pradesh",
            "India is the fifth largest economy",
            "Inflation rate in India is low as compare to other country"]

query = "Tell me about Delhi?"

doc_embedding = embeddings.embed_documents(document)
query_embedding = embeddings.embed_query(query)

#now find the similarity of query with the document
similarity_score = cosine_similarity([query_embedding], doc_embedding)[0]

#changing it into enum so the if order changed will find easily
index, score = (sorted(list(enumerate(similarity_score)),key=lambda x:x[1])[-1])

print("User Query : ", query)
print("Model Response : ", document[index])
#print(similarity_score)