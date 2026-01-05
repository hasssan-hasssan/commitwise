import requests

from requests.exceptions import Timeout, ConnectionError as ReqConnectionError

from commitwise.ai.base import AIEngine
from commitwise.errors import (
    AIProviderUnavailable,
    AIProviderTimeout,
    AIProviderConnectionError,
    AIProviderResponseInvalid,
)

DEFAULT_TIMEOUT = 60


class LocalAIEngine(AIEngine):
    """
    Local AI engine using Ollama.
    """

    def __init__(self, model: str, url: str):
        self.model = model
        self.url = url.rstrip("/")

    def generate_commit(self, diff: str) -> str:
        prompt = self.default_prompt + f"\n{diff}"

        try:
            response = requests.post(
                f"{self.url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=DEFAULT_TIMEOUT,
            )

        except Timeout:
            raise AIProviderTimeout(
                "Local AI model did not respond in time.\n\n "
                "Try staging fewer changes or using a faster model."
            )

        except ReqConnectionError:
            raise AIProviderUnavailable(
                "Local AI service is not reachable.\n\n "
                "Make sure Ollama is running (ollama serve)."
            )

        except Exception as exc:
            raise AIProviderConnectionError(
                f"Unexpected error while communicating with local AI: {exc}"
            ) from exc

        else:
            if response.status_code != 200:
                raise AIProviderUnavailable(
                    f"Local AI request failed with status {response.status_code}."
                )

            data = response.json()
            message = data.get("response", "").strip()

            if not message:
                raise AIProviderResponseInvalid(
                    "Local AI returned an empty commit message."
                )
            return message
