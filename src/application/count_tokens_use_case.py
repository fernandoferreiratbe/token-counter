from src.domain.token_counter import TokenCounter


class CounterTokensUseCase:

    def __init__(self, counter: TokenCounter):
        self.__counter = counter

    def count_tokens_from(self, prompt: str):
        return self.__counter.count_tokens_from(prompt=prompt)
