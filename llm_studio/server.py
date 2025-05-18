from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class LogRequest(BaseModel):
    text: str

@app.post("/analyze")
async def analyze_log(request: LogRequest):
    # Dummy logic: you can add LLM model calls here
    text = request.text.lower()
    suggestions = []
    if "error" in text:
        suggestions.append("Investigate error log")
    if "unauthorized" in text:
        suggestions.append("Check for access control issues")
    return {"suggestions": suggestions or ["No issues detected"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
