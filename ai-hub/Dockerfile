# Use an official Python image with 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for OpenCV and other libraries
RUN apt-get update && apt-get install -y \
    v4l-utils \
    ffmpeg \
    libsm6 \
    git \
    libxext6 \
    libgl1-mesa-glx \
    libgtk2.0-dev \
    libglib2.0-0 \
    libgtk-3-dev \
    python3-opencv \
    python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY ai-hub-models/qai_hub_models/ /app
COPY resize.py /app
COPY .env /app

# Install pip dependencies
RUN pip install opencv-python 

# Load environment variables
RUN set -a && . /app/.env && set +a && \
    pip install --upgrade pip && \
    pip install "$PIP_MODEL"

# for now, use particle SDK from git (FIXME after pypy)
RUN pip install git+https://github.com/particle-iot/particle-linux-python.git

# Ensure Python does not buffer output
ENV PYTHONUNBUFFERED=1

# Load environment variables and execute commands
ENTRYPOINT ["/bin/sh", "-c", "yes | $MODEL_CMD"]
#$PREFACE_CMD 4