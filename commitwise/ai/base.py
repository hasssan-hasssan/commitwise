from abc import ABC, abstractmethod


class AIEngine(ABC):
    """
    Base interface for AI enignes used by CommitWise
    """

    @abstractmethod
    def generate_commit(self, diff: str) -> str:
        """
        Generate a git commit message from a staged diff
        """

        raise NotImplementedError
