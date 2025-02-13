from typing import Type

import pytest

from src.domain.token_counter import TokenCounter


def test_call_abstract_method_should_raise_not_implement_error() -> None:
    with pytest.raises(NotImplementedError) as error:
        TokenCounter.count_tokens_from(Type[TokenCounter], prompt="foo")

    assert str(error.value) == "Method not implemented"
