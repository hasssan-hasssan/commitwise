from abc import ABC, abstractmethod


class AIEngine(ABC):
    """
    Base interface for AI enignes used by CommitWise
    """

    default_prompt: str = """
    You are generating a Git commit message.

    STRICT RULES:
        - Output ONLY the commit message text.
        - Do NOT include explanations, markdown, code fences, or extra text.
        - Do NOT say things like "Here is" or "This commit message".

    FORMAT:
        1. Use Conventional Commits format:
        <type>(<optional scope>): <short imperative summary>

        2. Allowed types:
        feat, fix, refactor, docs, test, chore

        3. The first line:
        - Must be imperative (e.g. add, fix, refactor, remove)
        - Must be concise and clear
        - Must be at most 72 characters

        4. If a body is needed:
        - Leave exactly one blank line after the title
        - Each line MUST start with "- "
        - Describe WHAT changed (not why)
        - Keep lines short and scannable

        5. Do NOT invent changes.
        - Only describe what is present in the staged diff.

    EXAMPLE OUTPUT:

        refactor(ai): centralize and enforce strict commit prompt

            - move AI commit prompt to base AIEngine
            - enforce clean, git-ready output rules
            - remove duplicated prompt logic from AI engines

    STAGED DIFF:

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
