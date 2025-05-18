import requests
import time
import os

LOG_DIR = "logs"
LLM_ENDPOINT = "http://127.0.0.1:7860/analyze"

def send_to_llm(log_data):
    try:
        response = requests.post(LLM_ENDPOINT, json={"text": log_data})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def monitor_logs():
    seen = set()
    while True:
        for filename in os.listdir(LOG_DIR):
            path = os.path.join(LOG_DIR, filename)
            if path not in seen and os.path.isfile(path):
                with open(path, "r") as f:
                    data = f.read()
                    result = send_to_llm(data)
                    print(f"LLM Suggestion for {filename}: {result}")
                seen.add(path)
        time.sleep(5)

if __name__ == "__main__":
    monitor_logs()