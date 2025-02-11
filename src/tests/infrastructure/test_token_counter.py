from src.domain.model_type import ModelType
from src.infrastructure.open_ai_token_counter import OpenAITokenCounter


def test_given_valid_model_type_and_prompt_should_return_tokens_quantity() -> None:
    token_counter = OpenAITokenCounter(model_type=ModelType.GPT_3_5_TURBO)
    prompt = """You are an software engineering. Write a code to put item into an amazon bucket s3 using Python."""
    # Expected value according to https://platform.openai.com/tokenizer
    expected_value = 21
    token_quantity = token_counter.count_tokens_from(prompt=prompt)

    assert token_quantity == expected_value, "Invalid token quantity"
