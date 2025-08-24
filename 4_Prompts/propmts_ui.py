import os
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import streamlit as st
from langchain_core.prompts import PromptTemplate


#setuping the download path
os.environ['HF_HOME'] = 'D:\Rajeshwar\HF_LOCAL_'

model_id = 'Qwen/Qwen3-0.6B'

llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task='text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 2000
    )
)

model = ChatHuggingFace(llm=llm)

st.header('Research Tool')
#query = st.text_input('Enter your prompts')

#using dyanamic prompt via priomptTemplate class
paper_input = st.selectbox("Select Research Paper Name : ",["Attention Is All YOU Need", 
                        "BERT: Pre-traning of Deep Bidirectional Transformer", 
                        "GPT-3: Language Models are Few-Short Learner"])

style_input = st.selectbox("Select Explanation Style", ["Begineer Friendly", "Technical", "mathematical"])

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", 
                                                           "Medium (3-5 paragraphs)", 
                                                           "Long (detailed explanation)"] )


template = PromptTemplate(
    template="""
    Please summarize the research paper titled {paper_input} with the following specifications:
    Explanation Style: {style_input}  
    Explanation Length: {length_input}  
    1. Mathematical Details:     
        - Include relevant mathematical equations if present in the paper.  
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
    2. Analogies:  
        - Use relatable analogies to simplify complex ideas.  
    If certain information is not available in the paper, respond with: Insufficient information available instead of guessing.  
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,
    input_variables=['paper_input', 'style_input', 'length_input']
)


#filling the place holder
prompt = template.invoke(
    {
        'paper_input' : paper_input,
        'style_input' : style_input,
        'length_input' : length_input
    }
)


if st.button('Summarize'):
    #response = model.invoke(f"Answer in 100 words only : {query}")
    response = model.invoke(prompt)
    answer = response.content

    if "</think>" in answer:
        answer = answer.split("</think>")[-1]
            
    st.write(answer)
    print("Output Fetched successfully.")
    


