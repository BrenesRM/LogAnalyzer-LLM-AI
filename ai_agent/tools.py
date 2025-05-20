# tools.py

import requests
from langchain.tools import Tool
from langchain.llms.base import LLM
from typing import List, Optional

# Load structured prompt template
with open("prompts/default.txt", "r") as f:
    STRUCTURED_PROMPT = f.read()

# Use a persistent session to improve performance
session = requests.Session()

# LangChain-compatible wrapper for local LLM
class LocalLLM(LLM):
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        try:
            response = session.post(
                "http://llm_service:5000/analyze",
                json={"log": prompt},  # The LLM service expects 'log'
                timeout=30
            )
            response.raise_for_status()
            json_data = response.json()
            return json_data["results"][0]["analysis"]
        except Exception as e:
            return f"❌ Error calling local LLM: {str(e)}"

    @property
    def _llm_type(self) -> str:
        return "local-llm"

# Custom tool function for analyzing logs
def analyze_log_entry(log_entry: str) -> str:
    full_prompt = STRUCTURED_PROMPT.replace("{{LOG_ENTRY}}", log_entry.strip())
    llm = LocalLLM()
    return llm(full_prompt)

# Expose the tool for LangChain Agent use
analyze_log_tool = Tool.from_function(
    func=analyze_log_entry,
    name="AnalyzeLog",
    description="Analyzes a raw log using structured cybersecurity assessment and MITRE ATT&CK mapping."
)

# Expose instances for reuse
local_llm_instance = LocalLLM()
