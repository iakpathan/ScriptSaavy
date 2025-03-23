from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
import os

# Load Groq API Key
api_key = os.getenv("GROQ_API_KEY")
llm = ChatGroq(model="llama3-8b-8192", api_key=api_key)

# LinkedIn Post Prompt
linkedin_prompt = PromptTemplate(
    input_variables=["topic"],
    template="""
Create a professional LinkedIn post on the following topic:

**Topic:** {topic}

**Requirements:**
- Be engaging, insightful, and suitable for a professional audience.
- Highlight key takeaways or relevant industry insights.
- Maintain a formal yet approachable tone.
- End with a call-to-action or thought-provoking question to encourage engagement.

**LinkedIn Post:**
"""
)

# Create LinkedIn Chain
def generate_linkedin_content(topic):
    response = linkedin_prompt | llm
    result = response.invoke({"topic": topic})
    return result
