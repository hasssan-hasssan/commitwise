from commitwise.config import (
    OPENAI_API_KEY,
    LOCAL_MODEL,
    LOCAL_API_URL,
)

from commitwise.ai.openai_engine import OpenAIEngine
from commitwise.ai.local_engine import LocalAIEngine
from commitwise.errors import AIError, AIProviderNotConfigured


def generate_ai_commit_message(diff: str) -> str:
    """
    Generate a git commit message using the best available AI provider.

    Priority:
    1. OpenAI (if OPENAI_API_KEY is set)
    2. Local AI (Ollama)

    Raises a clear error if no AI provider is available.
    """

    last_error: AIError | None = None

    # Try OpenAI
    if OPENAI_API_KEY:
        try:
            engine = OpenAIEngine(
                api_key=OPENAI_API_KEY,
                model="gpt-4.1-mini",
            )
            return engine.generate_commit(diff)
        except AIError as exc:
            last_error = exc

    # Fallback to Local AI
    if LOCAL_MODEL and LOCAL_API_URL:
        try:
            engine = LocalAIEngine(
                model=LOCAL_MODEL,
                url=LOCAL_API_URL,
            )
            return engine.generate_commit(diff)
        except AIError as exc:
            last_error = exc

    if last_error:
        raise last_error

    raise AIProviderNotConfigured(
        "No AI provider is configured.\n\n"
        "To use AI commits, you must either:\n"
        "- Set OPENAI_API_KEY to use OpenAI\n"
        "- Or install and run a local AI model (e.g. Ollama)\n\n"
        "https://ollama.com"
    )
