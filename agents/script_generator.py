import os
import warnings
from typing import Optional
from langchain.memory import ConversationSummaryBufferMemory
from langchain.tools import BaseTool
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# ✅ Suppress LangChain deprecation warnings
warnings.filterwarnings("ignore", category=UserWarning, module="langchain")

# ✅ Load environment variables correctly
load_dotenv()

# ✅ Load API key from .env file
api_key = os.getenv("GROQ_API_KEY")

# ✅ Check if API key is available
if not api_key:
    raise ValueError("API key is missing! Make sure to set GROQ_API_KEY in your .env file.")

# ✅ Initialize Groq model properly
llm = ChatGroq(api_key=api_key, model_name="llama3-8b-8192")

# ✅ Store conversation memory for multiple sessions
session_memory_store = {}


def get_session_memory(session_id, llm):
    """
    Retrieves or creates session memory for a given session.
    """
    if session_id not in session_memory_store:
        session_memory_store[session_id] = ConversationSummaryBufferMemory(
            llm=llm,
            memory_key="history",
            return_messages=True,
            max_token_limit=1000,
        )
    return session_memory_store[session_id]


# ✅ Corrected DummyTool with annotations
class DummyTool(BaseTool):
    name: str = "DummyTool"
    description: str = "A dummy tool that returns a default response."

    def _run(self, input_text: str) -> str:
        return "This is a placeholder response. No specific tool functionality provided."

    async def _arun(self, input_text: str) -> Optional[str]:
        return self._run(input_text)


from chains.chains import get_chain_and_generate

def generate_script(topic, duration=5, language='en', session_id="default"):
    """Generate a script with contextual memory."""
    try:
        result = get_chain_and_generate(topic, duration)

        # ✅ Check if result is an AIMessage object and extract content
        if hasattr(result, "content"):
            return result.content
        else:
            return str(result)

    except Exception as e:
        raise ValueError(f"Error while generating script: {str(e)}")



def chat_with_memory(message, session_id="default"):
    """Simulate chatbot response with session-based memory."""
    # ✅ Basic response simulation with memory (can be replaced with LLM logic)
    return f"Chatbot response to '{message}' in session '{session_id}'"
