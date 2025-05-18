LogAnalyzer-LLM-AI  
A powerful AI agent that leverages large language models (LLMs) to automatically analyze log files, identify anomalies, and suggest actionable mitigations. Powered by LLM Studio and the Qwen3-8B-Q4_K_M.gguf model, this tool is designed for cybersecurity professionals, system administrators, and researchers.  

🚀 Features  
Uses a local LLM (Qwen3-8B-Q4_K_M.gguf) for offline log analysis.  

Fully containerized via Docker & LLM Studio.  

Parses structured and semi-structured logs (e.g., syslog, Apache, custom).  

Identifies suspicious patterns, anomalies, and errors.  

Provides human-readable summaries and remediation suggestions.  

🧠 Model & Technology  
🔹 LLM: Qwen3-8B-Q4_K_M.gguf (quantized, optimized for inference)  

🔹 Framework: LLM Studio (local LLM orchestration)  

🔹 AI Agent: Task-driven assistant that interprets log content and suggests fixes  

🔹 Environment: Docker Compose for reproducibility and isolation  

🛠️ Installation  
1. Clone the Repository  
bash  
Copiar  
Editar  
git clone https://github.com/BrenesRM/LogAnalyzer-LLM-AI.git  
cd LogAnalyzer-LLM-AI

3. Download the Model  
Download the Qwen3-8B-Q4_K_M.gguf model and place it in the models directory.  

You can find it from Hugging Face or compatible repositories. Example:  

bash  
Copiar  
Editar  
mkdir -p models/qwen   
# Replace the URL below with the actual source  
wget -O models/qwen/Qwen3-8B-Q4_K_M.gguf https://huggingface.co/...  

3. Build and Launch the Environment  
Ensure you have Docker and Docker Compose installed:  

bash  
Copiar  
Editar  
docker-compose up --build  
This will:  

Start the LLM backend using LLM Studio  

Launch the AI log analysis agent  

📂 Usage  
Upload or specify the log file to analyze using the API or frontend (if implemented). Example:  

bash  
Copiar    
Editar  
curl -F "log=@/path/to/log.txt" http://localhost:8000/analyze  
The AI will return a structured JSON report with:  

📌 Detected issues  

🧠 Natural language summary  

✅ Suggested mitigations  

🧪 Example Output  
json  
Copiar  
Editar  
{  
  "summary": "Repeated failed SSH login attempts from 192.168.1.20",  
  "suggestions": [  
    "Block the IP address using the firewall",  
    "Check for signs of brute-force attack",  
    "Enable rate-limiting on SSH"  
  ],  
  "confidence_score": 0.93  
}  
📄 Security Analysis  
This project uses GitHub’s built-in security scanning. You can view the current status here.  

📜 License  
MIT License. See LICENSE for details.  
  
🙋‍♂️ Author  
Marlon Esteban Brenes Rojas  
Master's Student in Cybersecurity – NYIT Vancouver  
