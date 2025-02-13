from mockito import when

from src.application.count_tokens_use_case import CounterTokensUseCase
from src.domain.large_language_model import LargeLanguageModel
from src.domain.token_counter import TokenCounter
from src.infrastructure.open_ai_token_counter import OpenAITokenCounter


def test_count_token_through_use_case_should_return_1() -> None:
    openai_token_counter = OpenAITokenCounter(LargeLanguageModel.GPT_3_5_TURBO)
    prompt = "hello"
    when(openai_token_counter).count_tokens_from(prompt=prompt).thenReturn(1)
    counter_use_case = CounterTokensUseCase(counter=openai_token_counter)

    quantity = counter_use_case.count_tokens_from(prompt=prompt)

    assert quantity == 1
