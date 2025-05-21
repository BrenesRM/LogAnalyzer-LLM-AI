import requests

class LocalLlamaApi:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def chat(self, prompt: str, **kwargs) -> str:
        response = requests.post(self.endpoint, json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get("response", "")
        return f"Error: {response.status_code} {response.text}"
