import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


#setuping the download path
os.environ['HF_HOME'] = 'D:\Rajeshwar\HF_LOCAL_'

llm = HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task="text-generation",
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens=4000
    )
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("write an article on agentic ai in 3000 words.")

print(response.content)