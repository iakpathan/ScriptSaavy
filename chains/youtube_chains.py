from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

# Load Groq API Key
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama3-8b-8192", api_key=api_key)

# YouTube Vlog Chain
vlog_prompt = PromptTemplate(
    input_variables=["topic", "duration"],
    template="Write a {duration}-minute engaging YouTube Vlog script on {topic} with an intro, main content, and call to action."
)

# YouTube Podcast Chain
podcast_prompt = PromptTemplate(
    input_variables=["topic", "duration"],
    template="Write a {duration}-minute script for a YouTube Podcast on {topic} with detailed talking points and audience engagement."
)

# Create chains for vlog and podcast
def generate_youtube_vlog(topic, duration):
    vlog_chain = vlog_prompt | llm
    result = vlog_chain.invoke({"topic": topic, "duration": duration})
    return result

def generate_youtube_podcast(topic, duration):
    podcast_chain = podcast_prompt | llm
    result = podcast_chain.invoke({"topic": topic, "duration": duration})
    return result
