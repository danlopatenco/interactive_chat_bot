from langchain_community.document_loaders import BraveSearchLoader

from config.settings import BRAVE_API_KEY, COUNT_OF_BRAVE_SEARCH_RESPONSES


def brave_search(query: str):
    """
    Perform a Brave Search query asynchronously and return the content of the top results.

    Args:
        query (str): The search query.

    Returns:
        list: A list of page contents from the top search results.
    """
    loader = BraveSearchLoader(
        query=query,
        api_key=BRAVE_API_KEY,
        search_kwargs={"count": COUNT_OF_BRAVE_SEARCH_RESPONSES}
    )
    docs = loader.load()
    return [doc.page_content for doc in docs]
