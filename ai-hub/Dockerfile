# Use an official Python image with 3.11
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for OpenCV and other libraries
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY ai-hub-models/qai_hub_models/ /app
COPY resize.py /app

RUN pip install opencv-python

# Install Python dependencies (including YOLOv7 support)
RUN pip install --upgrade pip && \
    pip install "qai_hub_models[yolov7]"

# Ensure Python does not buffer output
ENV PYTHONUNBUFFERED=1

# Auto-accept repository cloning prompt using `yes`
ENTRYPOINT ["/bin/sh", "-c", "python resize.py images/fish.jpg && yes | python -m qai_hub_models.models.yolov7.demo --image images/fish.jpg --output-dir /app/output/"]