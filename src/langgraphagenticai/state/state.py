from typing import List, Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class State(TypeDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List,add_messages]


