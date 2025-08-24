from src.langgraphagenticai.state.state import State

class ChatbotwithToolNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role":"user", "content":user_input}])

        # simulate tool-specific logic
        tools_response = f"Tool Integration for :'{user_input}'"
        return {"messages":[llm_response,tools_response]}
    

    def create_chatbot(self,tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            chatbot logic for processing the input sttae and returning a response
            """

            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        
        return chatbot_node