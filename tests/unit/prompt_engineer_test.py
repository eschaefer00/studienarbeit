import pytest

from app.prompt_engineer import PromptEngineer


@pytest.fixture
def test_prompt():
    return "This is a test."


def test_define_art_style(test_prompt):
    prompt_engineer = PromptEngineer()
    result = prompt_engineer.define_art_style(test_prompt)

    assert isinstance(result, str)
    assert str.endswith(result, ", realistic art")
    assert result == test_prompt + ", realistic art"
