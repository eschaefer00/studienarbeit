import abc

from adapter.deep_l import AbstractDeepLAdapter


class AbstractPromptEngineer(abc.ABC):
    @abc.abstractmethod
    def define_art_style(self, prompt: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def translate_prompt(self, prompt: str) -> str:
        raise NotImplementedError


class PromptEngineer(AbstractPromptEngineer):
    def __init__(self, deep_l_adapter: AbstractDeepLAdapter):
        self.deep_l_adapter = deep_l_adapter

    def define_art_style(self, prompt: str) -> str:
        return self.translate_prompt(prompt) + ", high quality photo"

    def translate_prompt(self, prompt: str) -> str:
        translated_prompt = self.deep_l_adapter.translate_prompt(prompt)
        return translated_prompt
