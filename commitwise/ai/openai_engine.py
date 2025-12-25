from commitwise.ai.base import AIEngine


class OpenAIEngine(AIEngine):
    """
    OpenAI-based AI engine (optional).
    """

    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    def generate_commit(self, diff) -> str:
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError(
                "OpenAI SDK is not installed. Install it with: pip install openai"
            ) from exc
        client = OpenAI(api_key=self.api_key)

        prompt = self.default_prompt + f"\n{diff}"

        response = client.chat.completions.create(
            model=self.model,
            message=[
                {"role": "user", "content": prompt},
            ],
        )

        message = response.choices[0].message.content.strip()

        if not message:
            raise RuntimeError("OpenAI returned an empty commit message.")
        return message
