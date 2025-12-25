import os

# OpenAI configuration (optional)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Local AI (Ollama) configuration
LOCAL_MODEL = os.getenv("LOCAL_MODEL", "llama3")
LOCAL_API_URL = os.getenv("LOCAL_API_URL", "http://localhost:11434")
