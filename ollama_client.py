"""
ollama_client.py
Contains the reusable LLM client wrapper to communicate with the local Ollama model.
"""

from ollama import chat

# Custom exceptions for better error handling
class OllamaConnectionError(Exception):
    """Raised when the Ollama service is not running or unreachable."""
    pass

class OllamaModelError(Exception):
    """Raised when the requested model is not found locally."""
    pass

class OllamaLLM:
    """
    A reusable wrapper for the Ollama chat API.
    All agents will use this class to generate text.
    """
    def __init__(self, model="qwen3.5:9b"):
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the local Ollama model and returns the response.
        """
        try:
            response = chat(
                model=self.model,
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
            )
            # Extract and clean the text content
            return response.message.content.strip()
        
        except Exception as e:
            err_str = str(e).lower()
            # Handle connection errors
            if "connection" in err_str or "refused" in err_str or "connect" in err_str:
                raise OllamaConnectionError("Could not connect to Ollama.")
            # Handle model not found errors
            elif "not found" in err_str or "does not exist" in err_str:
                raise OllamaModelError(f"Model '{self.model}' not found.")
            # Handle other unexpected errors
            else:
                raise RuntimeError(f"Ollama error: {e}")