from flask import Flask, request, jsonify
from llama_cpp import Llama
import os
import sys
import signal

app = Flask(__name__)

# Load the LLM model
try:
    print("🧠 Loading Qwen3-8B-Q4_K_M model...")
    model_path = os.getenv("MODEL_PATH", "./models/Qwen3-8B-Q4_K_M.gguf")

    llm = Llama(
        model_path=model_path,
        n_ctx=2048,
        n_threads=4,
        n_gpu_layers=0
    )

except Exception as e:
    print(f"❌ Failed to load model: {e}", file=sys.stderr)
    sys.exit(1)

# Load the cybersecurity prompt template
TEMPLATE_PATH = os.getenv("PROMPT_TEMPLATE", "/app/prompts/log_analysis_prompt.txt")
try:
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        prompt_template = f.read()
except Exception as e:
    print(f"❌ Failed to load prompt template: {e}", file=sys.stderr)
    sys.exit(1)

# Graceful shutdown
def shutdown_handler(signum, frame):
    print("🛑 Shutting down cleanly...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown_handler)
signal.signal(signal.SIGTERM, shutdown_handler)

@app.route('/analyze', methods=['POST'])
def analyze_log():
    data = request.get_json()

    logs = data.get('log')
    if isinstance(logs, str):
        logs = [logs.strip()]
    elif isinstance(logs, list):
        # Ensure all elements are strings or dicts with a message
        logs = [entry.get("message", "").strip() if isinstance(entry, dict) else str(entry).strip() for entry in logs]
    else:
        return jsonify({"error": "'log' must be a string or a list"}), 400

    results = []

    for log_entry in logs:
        if not log_entry:
            continue

        prompt = prompt_template.replace("{{LOG_ENTRY}}", log_entry)

        try:
            output = llm(
                prompt,
                max_tokens=1024,
                temperature=0.7,
                top_p=0.9,
                echo=False
            )
            response_text = output["choices"][0]["text"].strip()
            results.append({
                "log": log_entry,
                "analysis": response_text
            })
        except Exception as e:
            results.append({
                "log": log_entry,
                "error": str(e)
            })

    return jsonify({"results": results})

if __name__ == '__main__':
    print("🚀 Log Analyzer API running on http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000)
