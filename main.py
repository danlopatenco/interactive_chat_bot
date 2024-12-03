from langchain_core.messages import HumanMessage, AIMessage

from config.settings import (
    LANGCHAIN_CONFIG,
    HUMAN_MESSAGE,
    AI_MESSAGE,
    USER_MESSAGE,
    STREAMLIT_CHAT_HISTORY_VARIABLE,
    STREAMED_CONTENT
)
from src.ai.flow import app
from src.web.streamlit_init import st


def main(st):
    if STREAMLIT_CHAT_HISTORY_VARIABLE not in st.session_state:
        st.session_state.chat_history = []

    if STREAMED_CONTENT not in st.session_state:
        st.session_state[STREAMED_CONTENT] = ""

    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message(HUMAN_MESSAGE):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message(AI_MESSAGE):
                st.markdown(message.content)

    user_query = st.chat_input(USER_MESSAGE)

    if user_query is not None and user_query != "":
        query = HumanMessage(user_query)
        st.session_state.chat_history.append(query)

        with st.chat_message(HUMAN_MESSAGE):
            st.markdown(user_query)

        with st.chat_message(AI_MESSAGE):
            input_messages = [query]
            state = {"messages": input_messages}

            ai_response_raw = app.invoke(state, LANGCHAIN_CONFIG)
            ai_response_output = AIMessage(ai_response_raw["messages"][-1].content)

            st.session_state.chat_history.append(ai_response_output)


if __name__ == "__main__":
    main(st)
