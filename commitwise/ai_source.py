from commitwise.config import (
    OPENAI_API_KEY,
    LOCAL_MODEL,
    LOCAL_API_URL,
)

from commitwise.ai.openai_engine import OpenAIEngine
from commitwise.ai.local_engine import LocalAIEngine


def generate_ai_commit_message(diff: str) -> str:
    """
    Generate a git commit message using the best available AI provider.

    Priority:
    1. OpenAI (if OPENAI_API_KEY is set)
    2. Local AI (Ollama)

    Raises a clear error if no AI provider is available.
    """
    # Try OpenAI
    if OPENAI_API_KEY:
        try:
            engine = OpenAIEngine(
                api_key=OPENAI_API_KEY,
                model="gpt-4.1-mini",
            )
            return engine.generate_commit(diff)
        except Exception as exc:
            raise RuntimeError(
                "Failed to generate commit message using OpenAI."
            ) from exc

    # Fallback to Local AI
    try:
        engine = LocalAIEngine(
            model=LOCAL_MODEL,
            url=LOCAL_API_URL,
        )
        return engine.generate_commit(diff)
    except Exception as exc:
        raise RuntimeError(
            "No AI provider available.\n\n"
            "To use AI commits, you must either:\n"
            "- Set OPENAI_API_KEY to use OpenAI\n"
            "- Or install and run a local AI model (e.g. Ollama)\n\n"
            "https://ollama.com"
        ) from exc
