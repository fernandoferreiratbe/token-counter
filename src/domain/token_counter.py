from abc import ABC, abstractmethod


class TokenCounter(ABC):

    @abstractmethod
    def count_tokens_from(self, prompt: str) -> int:
        ...
