import streamlit as st
from langflow.load import run_flow_from_json


TWEAKS = {
  "ChatInput-tyg1u": {},
  "Prompt-UfgZi": {},
  "OpenAIModel-A4s4A": {},
  "ChatOutput-VmLIe": {}
}

                            

# Initialize the LangFlow pipeline
st.title("LangFlow Application")
try:
    user_input = st.text_input("Enter your query:")
    result = run_flow_from_json(flow="Basic Prompting.json",
                            input_value=user_input,
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
    if user_input:
        response = pipeline.run(user_input)
        st.write("Response:", response)
except Exception as e:
    st.error(f"Error loading the LangFlow configuration: {e}")
