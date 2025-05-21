from google.adk.agents import LlmAgent
import yaml

# Load the YAML config
with open("agent.yaml", "r") as f:
    config = yaml.safe_load(f)

agent_config = config["agent"]

# ✅ Do not inject model here
agent = LlmAgent(**agent_config)

print(f"Agent '{agent.name}' initialized successfully.")

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        break
    try:
        print("Agent:", agent.chat(query))
    except Exception as e:
        print("Error:", e)
