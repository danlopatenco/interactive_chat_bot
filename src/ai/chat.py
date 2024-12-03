from langchain_core.messages import SystemMessage
from langgraph.graph import MessagesState
from langsmith import traceable

from config.settings import STREAMED_CONTENT
from src.ai.langchain_integration import model
from src.search.brave_search import brave_search
from src.web.streamlit_init import st


@traceable
def call_model(state: MessagesState):
    """Call the model and stream the response."""
    query = state["messages"][-1].content
    brave_search_results = brave_search(query)
    content = "\n".join(brave_search_results)
    system_message = SystemMessage(content=f"Content:\n{content}")
    messages = [system_message] + state["messages"]

    chunks = []

    placeholder = st.empty()

    for chunk in model.stream(messages):
        chunks.append(chunk.content)
        st.session_state[STREAMED_CONTENT] += chunk.content
        placeholder.markdown(st.session_state[STREAMED_CONTENT])

    full_response = " ".join(chunks)

    st.session_state[STREAMED_CONTENT] = ""
    return {"messages": full_response}
