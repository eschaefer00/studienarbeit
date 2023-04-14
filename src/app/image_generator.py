import abc

import requests
#from PIL import Image

from src.adapter.dall_e_2 import AbstractDallEAdapter


class AbstractImageGenerator(abc.ABC):
    @abc.abstractmethod
    def generate_image(self, prompt: str) -> str:
        raise NotImplementedError


class ImageGenerator(AbstractImageGenerator):
    def __init__(self, dall_e_adapter: AbstractDallEAdapter):
        self.dall_e_adapter = dall_e_adapter

    def generate_image(self, prompt: str) -> str:
        """
        > It takes a string as input, and returns a string as output

        :param prompt: The prompt to generate an image from
        :type prompt: str
        :return: A string
        """
        response = self.dall_e_adapter.create_image_from_prompt(prompt=prompt)
        return response["data"][0]["url"]

