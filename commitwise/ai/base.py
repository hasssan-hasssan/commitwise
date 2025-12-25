from abc import ABC, abstractmethod


class AIEngine(ABC):
    """
    Base interface for AI enignes used by CommitWise
    """

    default_prompt: str = """
    You are generating a git commit message.

    Rules:
    - Output ONLY the commit message text.
    - Do NOT include explanations.
    - Do NOT include markdown.
    - Do NOT include code fences.
    - Do NOT include phrases like "Here is" or "This commit message".

    Format:
    - First line: short imperative summary (max 72 chars)
    - Blank line
    - Optional detailed description

    Staged diff:
"""

    def __init__(self, prompt: str):
        # use provided prompt or default
        self.prompt = prompt or self.default_prompt

    @abstractmethod
    def generate_commit(self, diff: str) -> str:
        """
        Generate a git commit message from a staged diff
        """

        raise NotImplementedError
