import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get a response from LLAMA 2 Model

def getLLama(input_text,no_words,blog_style):
    llm = CTransformers(model="models\llama-2-7b-chat.ggmlv3.q6_K.bin",
                        model_type = "llama",
                        config={"max_new_tokens":256,
                                "temperature":0.01})
    
    ## Prompt Template
    template = """
        Write a blog for {blog_style} job profile for topic {input_text} 
        within {no_words} words.
         """
    
    prompt = PromptTemplate(
        input_variables = ['blog_style','input_text','no_words'],
        template = template
    )

    response = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blog",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')


st.header("Generate Blogs 🤖")
input_text = st.text_input("Enter The Blog Topic")

## Creating 2 more columns for additional fields

col1,col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of Words")

with col2:
    blog_style = st.selectbox("Writing The Blog for",("Researchers","Data Scientists","Common People"),index=0)


submit = st.button("Generate")

## Final Response 
if submit:
    st.write(getLLama(input_text,no_words,blog_style))