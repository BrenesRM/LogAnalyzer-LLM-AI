FROM python:3.10-slim

WORKDIR /app

# Install system dependencies first (build-essential needed for building some Python packages)
RUN apt-get update && apt-get install -y build-essential

# Upgrade pip, setuptools, wheel early
RUN pip install --upgrade pip setuptools wheel

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app files (including llm_wrappers.py and main.py)
COPY . .

# Install your local adk-python package (make sure ./adk-python exists relative to build context)
RUN pip install ./adk-python

CMD ["python", "main.py"]
