import abc

import deepl
from src.auth import deepl_auth_key


class AbstractDeepLAdapter(abc.ABC):
    @abc.abstractmethod
    def translate_prompt(self, prompt: str, src_lang: str = "DE", trgt_lang: str = "EN") -> str:
        raise NotImplementedError


class DeepLAdapter(AbstractDeepLAdapter):

    def __init__(self, api_key: str):
        deepl.auth_key = deepl_auth_key

    def translate_prompt(self, prompt: str, src_lang: str = "DE", trgt_lang: str = "EN-GB") -> str:
        """
        This function takes in a prompt, and returns a dictionary of the translation of the prompt

        :param trgt_lang: language acr to translate prompt into
        :type prompt: str
        :param src_lang: language acr to translate prompt from
        :type prompt: str
        :param prompt: The prompt is the text that you want to generate an image from
        :type prompt: str
        :return: A dictionary with the image url and the prompt.
        """
        translator = deepl.Translator(deepl_auth_key)
        result = translator.translate_text(text=prompt, source_lang=src_lang, target_lang=trgt_lang)
        return result.text
