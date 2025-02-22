import os
import unittest
from unittest.mock import MagicMock, patch
from openssm.integrations.openai.slm import GPT3ChatCompletionSLM, GPT3CompletionSLM, GPT4ChatCompletionSLM
from openssm.utils.config import Config


Config.OPENAI_API_URL = os.environ["OPENAI_API_URL"] = "test_url"
Config.OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] = "test_key"
Config.AZURE_GPT4_API_URL = os.environ["AZURE_GPT4_API_URL"] = "test_url"
Config.AZURE_GPT4_API_KEY = os.environ["AZURE_GPT4_API_KEY"] = "test_key"
Config.AZURE_GPT4_ENGINE = os.environ["AZURE_GPT4_ENGINE"] = "test_engine"


# pylint: disable=protected-access

class TestGPT3CompletionSLM(unittest.TestCase):
    def test_constructor_default_values(self):
        slm = GPT3CompletionSLM()
        self.assertEqual(slm.api_context.key, "test_key")
        self.assertEqual(slm.api_context.base, "test_url")
        self.assertEqual(slm.api_context.model, "text-davinci-002")

    @patch('openai.Completion.create')
    def test_call_lm_api(self, mock_create):
        fake_response = MagicMock()
        fake_response.choices[0].text = "Test Response"
        mock_create.return_value = fake_response
        slm = GPT3CompletionSLM()
        conversation = [{'content': 'Test Content'}]
        response = slm._call_lm_api(conversation)
        self.assertEqual(response["content"], "Test Response")


class TestGPT3ChatCompletionSLM(unittest.TestCase):
    def test_constructor_default_values(self):
        slm = GPT3ChatCompletionSLM()
        self.assertEqual(slm.api_context.key, "test_key")
        self.assertEqual(slm.api_context.base, "test_url")
        self.assertEqual(slm.api_context.model, "gpt-3.5-turbo")

    @patch('openai.ChatCompletion.create')
    def test_call_lm_api(self, mock_create):
        fake_response = MagicMock()
        fake_response.choices[0].message = "Test Response"
        mock_create.return_value = fake_response
        slm = GPT3ChatCompletionSLM()
        conversation = [{'content': 'Test Content'}]
        response = slm._call_lm_api(conversation)
        self.assertEqual(response, "Test Response")


class TestGPT4ChatCompletionSLM(unittest.TestCase):
    def test_constructor_default_values(self):
        slm = GPT4ChatCompletionSLM()
        self.assertEqual(slm.api_context.key, "test_key")
        self.assertEqual(slm.api_context.base, "test_url")
        self.assertEqual(slm.api_context.engine, "test_engine")

    @patch('openai.ChatCompletion.create')
    def test_call_lm_api(self, mock_create):
        fake_response = MagicMock()
        fake_response.choices[0].message = "Test Response"
        mock_create.return_value = fake_response
        slm = GPT4ChatCompletionSLM()
        conversation = [{'content': 'Test Content'}]
        response = slm._call_lm_api(conversation)
        self.assertEqual(response, "Test Response")
