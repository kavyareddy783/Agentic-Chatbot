import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langraph_agenticai_app():
    """

    """

    ## Load UI 

    ui = LoadStreamlitUI()
    user_input = ui.load_steamlit_ui()


    if not user_input:
        st.error("Error: Failed to load user input from the UI")
        return 
    
    user_message = st.chat_input("Enter your message:")
