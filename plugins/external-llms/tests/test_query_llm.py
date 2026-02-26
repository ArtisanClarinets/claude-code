import unittest
import sys
import os
import json
from unittest.mock import patch, MagicMock

# Add the scripts directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

import query_llm

class TestQueryLLM(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_query_openai_compatible(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "choices": [{"message": {"content": "Hello world"}}]
        }).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        api_key = "test_key"
        base_url = "https://api.openai.com" # Base URL without /v1/chat/completions
        model = "gpt-4"
        prompt = "Hello"

        # Note: query_openai_compatible handles adding /v1/chat/completions or /chat/completions
        result = query_llm.query_openai_compatible(api_key, base_url, model, prompt)

        self.assertEqual(result, "Hello world")

        # Verify request
        args, kwargs = mock_urlopen.call_args
        req = args[0]
        # Depending on implementation, it might append /v1/chat/completions
        self.assertTrue(req.full_url.endswith("/chat/completions"))
        self.assertEqual(req.headers['Authorization'], "Bearer test_key")

        data = json.loads(req.data.decode('utf-8'))
        self.assertEqual(data['model'], "gpt-4")
        self.assertEqual(data['messages'][0]['content'], "Hello")

    @patch('urllib.request.urlopen')
    def test_query_gemini(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "candidates": [{"content": {"parts": [{"text": "Gemini says hi"}]}}]
        }).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        api_key = "gemini_key"
        model = "gemini-pro"
        prompt = "Explain quantum physics"

        result = query_llm.query_gemini(api_key, model, prompt)

        self.assertEqual(result, "Gemini says hi")

        # Verify request
        args, kwargs = mock_urlopen.call_args
        req = args[0]
        self.assertIn("generativelanguage.googleapis.com", req.full_url)
        self.assertIn("key=gemini_key", req.full_url)

        data = json.loads(req.data.decode('utf-8'))
        self.assertEqual(data['contents'][0]['parts'][0]['text'], "Explain quantum physics")

    @patch('urllib.request.urlopen')
    def test_query_ollama(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "response": "Llama runs locally"
        }).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        base_url = "http://localhost:11434"
        model = "llama3"
        prompt = "Why is the sky blue?"

        result = query_llm.query_ollama(base_url, model, prompt)

        self.assertEqual(result, "Llama runs locally")

        # Verify request
        args, kwargs = mock_urlopen.call_args
        req = args[0]
        self.assertEqual(req.full_url, "http://localhost:11434/api/generate")

        data = json.loads(req.data.decode('utf-8'))
        self.assertEqual(data['model'], "llama3")
        self.assertEqual(data['prompt'], "Why is the sky blue?")

    @patch('urllib.request.urlopen')
    def test_query_anthropic(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({
            "content": [{"text": "Claude says hi"}]
        }).encode('utf-8')
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        api_key = "anthropic_key"
        model = "claude-3-opus"
        prompt = "Hello Claude"

        result = query_llm.query_anthropic(api_key, model, prompt)

        self.assertEqual(result, "Claude says hi")

        # Verify request
        args, kwargs = mock_urlopen.call_args
        req = args[0]
        self.assertEqual(req.full_url, "https://api.anthropic.com/v1/messages")

        # Check headers case-insensitively
        headers = {k.lower(): v for k, v in req.headers.items()}
        self.assertEqual(headers['x-api-key'], "anthropic_key")
        self.assertEqual(headers['anthropic-version'], "2023-06-01")

        data = json.loads(req.data.decode('utf-8'))
        self.assertEqual(data['model'], "claude-3-opus")
        self.assertEqual(data['messages'][0]['content'], "Hello Claude")

if __name__ == '__main__':
    unittest.main()
