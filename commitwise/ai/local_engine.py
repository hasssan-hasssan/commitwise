import requests

from commitwise.ai.base import AIEngine


class LocalAIEngine(AIEngine):
    """
    Local AI engine using Ollama.
    """

    def __init__(self, model: str, url: str):
        self.model = model
        self.url = url.rstrip("/")

    def generate_commit(self, diff: str) -> str:
        prompt = self.default_prompt + f"\n{diff}"

        response = requests.post(
            f"{self.url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=60,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Local AI request failed (status {response.status_code})"
            )

        data = response.json()
        message = data.get("response", "").strip()

        if not message:
            raise RuntimeError("Local AI returned an empty commit message.")

        return message
