from flask import Flask, request, jsonify
import yaml
from google.adk.agents import LlmAgent  # explicitly using LlmAgent

# Load the YAML config
with open("agent.yaml", "r") as f:
    config = yaml.safe_load(f)

# Access the nested agent configuration
agent_config = config["agent"]

# Initialize the agent
agent = LlmAgent(**agent_config)

print(f"Agent '{agent.name}' initialized successfully.")
