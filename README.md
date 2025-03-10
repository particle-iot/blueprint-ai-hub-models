# **Qualcomm AI Hub Models - Particle Blueprint**

## **Introduction**
Welcome to the **Qualcomm AI Hub Models Blueprint App**! This project enables **AI model execution** from [Qualcomm's AI Hub Models](https://github.com/quic/ai-hub-models) on **Linux-based edge devices** using **Particle's IoT platform**.

With this blueprint, you can:
- **Deploy and run AI models** dynamically from the AI Hub.
- **Use Docker to containerize execution**, making it easy to manage and update.
- **Leverage Particle's IoT platform** for remote deployment and model selection.

This serves as an **entry point** for running AI workloads at the edge using **Tachyon** and **other supported Linux devices**.

---

## **Project Structure**
The repository is structured as follows:

```
/ai-hub
│── /ai-hub-models/        # The AI Hub Models repository (submodule)
│    ├── qai_hub_models/   # Core AI Hub framework
│    ├── configs/          # AI model configuration files
│    ├── datasets/         # Dataset handling for AI training/inference
│    ├── models/           # Model definitions and implementations
│    ├── scripts/          # Utility scripts for setup and execution
│    ├── Dockerfile        # Docker container setup
│    ├── README.md         # AI Hub-specific documentation
│── docker-compose.yaml    # Docker Compose setup
│── output/                # Stores inference results
│── images/                # Example images for model testing
│── blueprint.yaml         # Particle Blueprint definition
│── README.md              # This document
```

### **AI Hub Models as a Submodule**
The [AI Hub Models](https://github.com/quic/ai-hub-models) are pulled in as a **Git submodule** within this repository. This allows easy updates and synchronization with the latest developments from Qualcomm's AI Hub.

To ensure you have the latest submodule contents, run:
```sh
git submodule update --init --recursive
```

---

## **Getting Started: Running AI Models**
This blueprint allows you to **execute AI models** using **Docker containers** on **Particle-supported edge devices**.

### **1. Set Up Your Particle Linux Device**
Ensure your **Tachyon** or **Raspberry Pi** device is:
- Running a compatible **Linux distribution**.
- Connected to the **Particle IoT platform**.

### **2. Clone & Initialize the Submodules**
Since this repo includes a submodule, use:
```sh
git clone --recurse-submodules https://github.com/particle-iot/blueprint-ai-hub-models.git
cd blueprint-ai-hub-models
```

If you've already cloned the repository but forgot the submodule, run:
```sh
git submodule update --init --recursive
```

### **3. Build & Run the Docker Container**
Use Docker Compose to build and run the container:
```sh
docker-compose up --build
```

To run a specific model:
```sh
particle app run
```

For details on available models, refer to the [original AI Hub Models](https://github.com/quic/ai-hub-models/tree/main/qai_hub_models/models).

---

## **Contributions**
We welcome contributions! If you have improvements or fixes, please open a **pull request** in the [AI Hub Models GitHub Repository](https://github.com/quic/ai-hub-models).

---

## **Supported Devices**
This blueprint supports:
- **Tachyon** (Particle Linux Edge Device)
- **Raspberry Pi**
- Other **Linux-based edge computing platforms**
