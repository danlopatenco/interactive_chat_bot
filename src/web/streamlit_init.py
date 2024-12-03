import streamlit as st

from config.settings import (
    PAGE_TITLE,
)

st.set_page_config(page_title=PAGE_TITLE)
st.title(PAGE_TITLE)
