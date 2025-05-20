FROM python:3.11-slim

# Install build tools and libcurl
RUN apt-get update && apt-get install -y \
    git cmake build-essential wget curl \
    libcurl4-openssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Clone llama.cpp and build it
WORKDIR /llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp . && \
    cmake . -Bbuild && cmake --build build -j && \
    pip install .

# Set up app directory
WORKDIR /app

# Copy application files
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY models /app/models
COPY prompts /app/prompts

# Install Python dependencies
RUN pip install -r requirements.txt

# Default command
CMD ["python", "app.py"]
