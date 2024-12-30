import streamlit as st

# Load your LangFlow configuration JSON file
flow_file_path = "Basic Prompting.json"  # Replace with your file path

# Initialize the LangFlow pipeline
st.title("LangFlow Application")
try:
    user_input = st.text_input("Enter your query:")
    if user_input:
        st.write("Response:")
except Exception as e:
    st.error(f"Error loading the LangFlow configuration: {e}")
