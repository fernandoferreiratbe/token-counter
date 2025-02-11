import tiktoken

from src.domain.model_type import ModelType
from src.domain.token_counter import TokenCounter


class GPT4oTokenCounter(TokenCounter):

    def __init__(self, model_type: ModelType):
        self.__model_type = str(model_type.value)

    def count_tokens_from(self, prompt: str) -> int:
        """
        Conta o número de tokens em um prompt usando a biblioteca tiktoken.

        Args:
        prompt: O prompt para o qual contar os tokens (string).
        modelo: O nome do modelo para o qual contar os tokens (string, opcional).
            O padrão é "gpt-3.5-turbo".

        Returns:
        O número de tokens no prompt (inteiro).
        """

        try:
            # Codificação específica para modelos OpenAI
            encoding = tiktoken.encoding_for_model(self.__model_type)
        except KeyError:
            # Caso o modelo não seja reconhecido, usa a codificação padrão
            print(f"Modelo '{self.__model_type}' não encontrado. Usando codificação 'cl100k_base'.")
            encoding = tiktoken.get_encoding("cl100k_base")

        # Contar tokens
        num_tokens = len(encoding.encode(prompt))

        return num_tokens

