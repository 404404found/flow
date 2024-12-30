from langflow.load import run_flow_from_json
TWEAKS = {
  "ChatInput-tyg1u": {
    "background_color": "",
    "chat_icon": "",
    "files": "",
    "input_value": "How are you?",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "Prompt-UfgZi": {
    "template": "Answer the user as if you were a GenAI expert, enthusiastic about helping them get started building something fresh."
  },
  "OpenAIModel-A4s4A": {
    "api_key": "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",
    "input_value": "",
    "json_mode": False,
    "max_tokens": None,
    "model_kwargs": {},
    "model_name": "gpt-4o-mini",
    "openai_api_base": "",
    "output_schema": {},
    "seed": 1,
    "stream": False,
    "system_message": "",
    "temperature": 0.1
  },
  "ChatOutput-VmLIe": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  }
}

result = run_flow_from_json(flow="Basic Prompting.json",
                            session_id="", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
