import tiktoken

from src.domain.large_language_model import LargeLanguageModel
from src.domain.token_counter import TokenCounter


class OpenAITokenCounter(TokenCounter):

    def __init__(self, large_language_model: LargeLanguageModel):
        self.__large_language_model = str(large_language_model.value)

    def count_tokens_from(self, prompt: str) -> int:
        """
        Count the token quantity of a prompt using tiktoken library

        Args:
            prompt: instructions to LLM model in text format

        Returns:
            The number of tokens in a prompt
        """

        try:
            encoding = tiktoken.encoding_for_model(self.__large_language_model)
        except KeyError:
            print(f"Model '{self.__large_language_model}' not found. Change encoding to 'cl100k_base'.")
            encoding = tiktoken.get_encoding("cl100k_base")

        tokens_quantity = len(encoding.encode(prompt))

        return tokens_quantity
