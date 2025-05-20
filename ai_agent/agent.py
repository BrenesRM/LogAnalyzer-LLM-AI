from flask import Flask, request, jsonify, make_response
from langchain.agents import initialize_agent, AgentType
from tools import analyze_log_tool, local_llm_instance, session

# Initialize the agent once for both CLI and Flask
agent = initialize_agent(
    tools=[analyze_log_tool],
    llm=local_llm_instance,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def process_log_entry(log_entry: str):
    # You might want to prepend instructions here if needed
    return agent.run(f"Use the AnalyzeLog tool to assess this log: {log_entry}")

def run_cli():
    try:
        while True:
            print("\nEnter a raw log entry to analyze (or type 'exit'):")
            user_input = input("> ").strip()
            if user_input.lower() in ["exit", "quit"]:
                print("🛑 Exiting agent.")
                break
            result = process_log_entry(user_input)
            print(f"\n📘 Structured Security Report:\n{result}\n")

    except KeyboardInterrupt:
        print("\n🛑 Interrupted by user. Shutting down.")
    finally:
        session.close()

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data or 'log' not in data:
        response = make_response(jsonify({"error": "Missing 'log' in request JSON"}), 400)
        response.headers['Connection'] = 'close'
        return response

    log_entry = data['log']
    analysis = process_log_entry(log_entry)
    response = make_response(jsonify({"analysis": analysis}))
    response.headers['Connection'] = 'close'
    return response

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'cli':
        run_cli()
    else:
        app.run(host='0.0.0.0', port=5002)
