import os

from dotenv import load_dotenv

from src.utils import get_env_var, get_int_env_var

load_dotenv()

# Open AI
OPEN_AI_API_KEY = get_env_var('OPEN_AI_API_KEY')

# Langchain
LANGCHAIN_CONFIG = {"configurable": {"thread_id": "some_tread_id"}}

# Brave Search
COUNT_OF_BRAVE_SEARCH_RESPONSES = get_int_env_var('COUNT_OF_BRAVE_SEARCH_RESPONSES')
BRAVE_API_KEY = get_env_var('BRAVE_API_KEY')

# LangSmith
LANGCHAIN_TRACING_V2 = get_env_var('LANGCHAIN_TRACING_V2', "false")
LANG_SMITH_KEY = get_env_var('LANG_SMITH_KEY')

os.environ["LANGCHAIN_TRACING_V2"] = LANGCHAIN_TRACING_V2
os.environ["LANGCHAIN_API_KEY"] = LANG_SMITH_KEY

# Streamlit configution
PAGE_TITLE = "Interactive Chatbot with Memory and Web Search"
STREAMLIT_CHAT_HISTORY_VARIABLE = "chat_history"
STREAMED_CONTENT = "streamed_content"
HUMAN_MESSAGE = 'Human'
AI_MESSAGE = 'AI'
USER_MESSAGE = "You:"
