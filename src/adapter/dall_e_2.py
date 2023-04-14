import abc

import openai
from auth import auth_key


class AbstractDallEAdapter(abc.ABC):
    @abc.abstractmethod
    def create_image_from_prompt(self, prompt: str, size: str = "512x512") -> dict:
        raise NotImplementedError


class DallEAdapter(AbstractDallEAdapter):

    def __init__(self, api_key: str):
        openai.api_key = auth_key

    def create_image_from_prompt(self, prompt: str, size: str = "512x512") -> dict:
        """
        This function takes in a prompt and a size, and returns a dictionary of the image created by the prompt

        :param prompt: The prompt is the text that you want to generate an image from
        :type prompt: str
        :param size: The size of the image to generate, defaults to 512x512
        :type size: str (optional)
        :return: A dictionary with the image url and the prompt.
        """
        response = openai.Image.create(prompt=prompt, n=1, size=size)
        return response
