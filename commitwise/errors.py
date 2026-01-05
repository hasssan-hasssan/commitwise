"""
Centralized error definitions for CommitWise.

All domain-level errors should live here.
CLI layer is responsible for translating these errors
into user-friendly message
"""


class CommitWiseError(Exception):
    """Base exception for all CommitWise erros."""

    pass


class NoStagedChangesError(CommitWiseError):
    """Raised when no changes are staged for commit."""

    pass


class InvalidUsageError(CommitWiseError):
    """Raised when CLI arguments or usage is invalid"""

    pass


class UserAbortError(CommitWiseError):
    """Raised when user aborts an action (e.g. commit confirmation)"""

    pass


class AIError(CommitWiseError):
    """Base exception for all AI-related error"""

    pass


class AIProviderNotConfigured(AIError):
    """
    No AI provider is configured.

    Example:
    - No OPENAI_API_KEY
    - Ollama not installed
    """

    pass


class AIProviderUnavailable(AIError):
    """
    Provider exists but not reachable.

    Example:
    - Ollama installed but service not running
    - OpenAI endpoint unreachable
    """

    pass


class AIProviderTimeout(AIError):
    """
    Provider did not respond in time.

    Common causes:
    - Large diff
    - Slow local inference
    - Network latency
    """

    pass


class AIProviderConnectionError(AIError):
    """
    Connection failed during request.

    Example:
    - Connection reset
    - DNS failure
    """

    pass


class AIProviderResponseInvalid(AIError):
    """
    AI responded but output is invalid or empty.
    """

    pass


class AIProviderAuthError(AIError):
    """Invalid or missing AIProvider API key"""

    pass


class AIProviderRateLimitError(AIError):
    """AIProvider rate limit exceeded"""

    pass
