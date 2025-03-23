import requests
from bs4 import BeautifulSoup
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY, SERPAPI_API_KEY, SEARCH_API_URL

# Initialize Groq API with the correct model
llm = ChatGroq(model_name="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


# Web Search Using SerpAPI
def web_search(query: str) -> str:
    """Performs a web search using SerpAPI and returns top 5 results."""
    url = f"{SEARCH_API_URL}?q={query}&api_key={SERPAPI_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        search_results = data.get("organic_results", [])

        # Extract top 5 URLs and titles
        results = []
        for i, result in enumerate(search_results[:5]):
            title = result.get("title")
            link = result.get("link")
            results.append(f"{i+1}. {title} - {link}")

        return "\n".join(results)
    else:
        return "Error retrieving search results. Check API key or query."

# Scrape and Extract Relevant Content
def scrape_and_summarize(url: str) -> str:
    """Scrapes and summarizes content from the provided URL."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error: Unable to fetch URL. Status Code: {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = "\n".join([p.get_text() for p in paragraphs[:10]])

        if not content.strip():
            return "No relevant content found on the page."

        # Summarize content using LLM
        summary_prompt = f"Summarize the following content:\n{content}\nProvide a concise summary."
        summary = llm.predict(summary_prompt)

        return summary
    except Exception as e:
        return f"Error fetching content: {str(e)}"

# Define Tools
tools = [
    Tool(name="Web Search", func=web_search, description="Search the internet and retrieve results"),
    Tool(name="Scrape and Summarize", func=scrape_and_summarize, description="Scrape and summarize content from URLs")
]

# Initialize Internet Agent
internet_agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

