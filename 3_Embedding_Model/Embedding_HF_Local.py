from langchain_huggingface import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
#setuping the download path
os.environ['HF_HOME'] = 'D:\Rajeshwar\HF_LOCAL_'

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

#single line text
#text = "Delhi is the capital fof India"

#multi-line text
document = ["Delhi is the capital fof India",
            "Lucknow is the capital of Uttar Pradesh",
            "India is the fifth largest economy",
            "Inflation rate in India is low as compare to other country"]

#vector = embedding.embed_query(text=text)

vector = embedding.embed_documents(document)
print(str(vector))