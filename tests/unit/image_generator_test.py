import validators

from adapter.dall_e_2 import AbstractDallEAdapter
from app.image_generator import ImageGenerator


class TestDallEAdapter(AbstractDallEAdapter):
    def create_image_from_prompt(self, prompt: str, size: str = "512x512") -> dict:
        return {"data": [{"url": "https://google.de"}]}


def test_generate_image():
    dall_2_adapter = TestDallEAdapter()
    image_generator = ImageGenerator(dall_e_adapter=dall_2_adapter)

    result = image_generator.generate_image(prompt="Testprompt")

    assert isinstance(result, str)

    assert validators.url(result)
