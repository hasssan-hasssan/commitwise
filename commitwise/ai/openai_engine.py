from commitwise.ai.base import AIEngine
from commitwise.errors import (
    AIProviderNotConfigured,
    AIProviderAuthError,
    AIProviderRateLimitError,
    AIProviderTimeout,
    AIProviderConnectionError,
    AIProviderResponseInvalid,
)


from openai import OpenAI
from openai import (
    AuthenticationError,
    RateLimitError,
    APIConnectionError,
    APITimeoutError,
    OpenAIError,
)


class OpenAIEngine(AIEngine):
    """
    OpenAI-based AI engine (optional).
    """

    def __init__(self, api_key: str, model: str):
        if not api_key:
            raise AIProviderNotConfigured("OPENAI_API_KEY is not set.")

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate_commit(self, diff) -> str:
        prompt = self.default_prompt + f"\n{diff}"
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt},
                ],
            )
        except AuthenticationError:
            raise AIProviderAuthError("Invalid OpenAI API key.")

        except RateLimitError:
            raise AIProviderRateLimitError("OpenAI rate limit exceeded.")

        except APITimeoutError:
            raise AIProviderTimeout("OpenAI request timed out.")

        except APIConnectionError:
            raise AIProviderConnectionError("Failed to connect to OpenAI API.")

        except OpenAIError as exc:
            raise AIProviderConnectionError(f"Unexpected OpenAI error: {exc}") from exc

        try:
            message = response.choices[0].message.content.strip()
        except Exception:
            raise AIProviderResponseInvalid("OpenAI returned an invalid response.")

        if not message:
            raise AIProviderResponseInvalid("OpenAI returned an empty commit message.")

        return message
