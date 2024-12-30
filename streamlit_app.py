import streamlit as st
from langflow import load_flow

# Load your LangFlow configuration JSON file
flow_file_path = "Basic Prompting.json"  # Replace with your file path

# Initialize the LangFlow pipeline
st.title("LangFlow Application")
try:
    pipeline = load_flow(flow_file_path)
    user_input = st.text_input("Enter your query:")
    if user_input:
        response = pipeline.run(user_input)
        st.write("Response:", response)
except Exception as e:
    st.error(f"Error loading the LangFlow configuration: {e}")
