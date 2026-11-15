# Microsoft Foundry & Azure AI Services: Hands-On Project

A hands-on project where I learned and implemented the end-to-end development of AI solutions on **Microsoft Foundry** and **Azure AI services**, from platform setup to advanced agentic workflows.

![Microsoft Foundry](https://img.shields.io/badge/Microsoft-Foundry-0078D4?logo=microsoftazure&logoColor=white)
![Azure AI Search](https://img.shields.io/badge/Azure-AI%20Search-0078D4)
![LangChain](https://img.shields.io/badge/LangChain-Integrated-1C3C3C)
![MCP](https://img.shields.io/badge/MCP-Tools-blueviolet)

## What I Built and Learned

### 1. Platform Foundations
- Understood the **Microsoft Foundry architecture** and its role in modern AI engineering
- Set up a **free Azure account** and navigated the Foundry portal

### 2. AI Model Management
- **Deployed LLMs** to the Foundry environment
- Configured **LLM access via APIs** for scalable model interaction
- Integrated Foundry-hosted models with **LangChain** for application development

### 3. Azure AI Services (Cognitive Services)
Implemented and tested:
- **OCR**: extracting text from images and documents
- **Text-to-Speech (TTS)**
- **Speech-to-Text (STT)**
- **Live Translation**

### 4. Search and RAG Architecture
- Set up **Azure AI Search** indexes and pipelines
- Built a **Retrieval-Augmented Generation (RAG)** workflow to answer questions over proprietary data

### 5. Advanced Agentic AI
- **Foundry IQ**: used knowledge bases to give agents context-aware responses
- **Foundry Agents**: designed custom agents for automated task execution
- **Model Context Protocol (MCP)**: implemented MCP tools to extend agent capabilities and interoperability

## Tech Stack

| Area | Tools |
|------|-------|
| Platform | Microsoft Foundry, Azure AI Foundry |
| Models | Azure-deployed LLMs via API |
| Frameworks | LangChain, MCP |
| AI Services | OCR, TTS, STT, Live Translation |
| Search / RAG | Azure AI Search |
| Language | Python |

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/iamsuraj24-hub/<your-repo-name>.git
cd <your-repo-name>

# 2. Install uv (if not already installed)
# https://docs.astral.sh/uv/getting-started/installation/

# 3. Install dependencies (creates a virtual environment automatically)
uv sync

# 4. Configure environment variables
cp .env.example .env
# Add your Azure endpoint and API key to .env
```

## Credits
Learned by following the Microsoft Foundry masterclass by Ansh Lamba ([YouTube link](https://www.youtube.com/watch?v=nuQtFrewR0o)). All implementation and experiments in this repo were done by me while following and extending the course.

## Author
**Suraj Gupta**: AI/ML Engineer
[LinkedIn](https://www.linkedin.com/in/suraj-gupta-ai-ml-engineer) | [GitHub](https://github.com/iamsuraj24-hub)
