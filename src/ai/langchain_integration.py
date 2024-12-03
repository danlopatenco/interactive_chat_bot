from langchain_openai import ChatOpenAI

from config.settings import OPEN_AI_API_KEY
from src.ai.enums import ModelType

model = ChatOpenAI(model=ModelType.GPT_4O_MINI, openai_api_key=OPEN_AI_API_KEY, streaming=True)
