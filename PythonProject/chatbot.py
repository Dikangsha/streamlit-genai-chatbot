import os

from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load the environment variables
load_dotenv()

# Streamlit page setup
st.set_page_config(
    page_title="🤖 Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Generative AI Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# LLM initialize
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.0,
)

# Input box
user_prompt = st.chat_input("Ask Chatbot...")

if user_prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Save user message to chat history
    st.session_state.chat_history.append(
        {"role": "user", "content": user_prompt}
    )

    # Send chat history to LLM
    response = llm.invoke(
        [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
        + st.session_state.chat_history
    )

    assistant_response = response.content

    # Save response in chat history
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_response}
    )

    # Display LLM response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)