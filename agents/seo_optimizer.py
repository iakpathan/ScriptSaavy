import os
from langchain.llms import Groq

groq_api_key = os.getenv('GROQ_API_KEY')
llm = Groq(api_key=groq_api_key)

# Load SEO Template
with open('templates/seo_template.txt', 'r') as f:
    SEO_PROMPT_TEMPLATE = f.read()

def optimize_seo(content):
    prompt = SEO_PROMPT_TEMPLATE.format(content=content)
    response = llm.predict(prompt)
    return response
