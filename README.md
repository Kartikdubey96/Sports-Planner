# 🏏 Sports-Planner: AI Agentic Framework (Group G10D5)

This repository contains a high-performance **Dockerized Multi-Agent Sports Analysis System**. [cite_start]Originally proposed as a Rust service[cite: 3], the project has been evolved into a sophisticated **Python-based Agentic Framework** using **CrewAI**, **Streamlit**, and **Google Gemini**. [cite_start]It is fully automated via **GitHub Actions** and hosted on **AWS EC2**[cite: 48].

---

## 🚀 Live Cloud Deployment
**Production URL:** [http://<YOUR-EC2-PUBLIC-IP>:8501](http://<YOUR-EC2-PUBLIC-IP>:8501)

## 📁 Project Structure & Documentation
* [cite_start][**📜 Final Project Report (PDF)**](./docs/Project%20Report%20DO_10.pdf) - Official Technical Documentation[cite: 13].
* [**🐍 agents.py**](./agents.py) - Definitions for the **Researcher** and **Writer** agents.
* [**🌐 app.py**](./app.py) - Streamlit Web Interface (Frontend).
* [cite_start][**🐳 Dockerfile**](./Dockerfile) - Containerization instructions for consistent deployment[cite: 53].
* [cite_start][**⚙️ deploy.yml**](./.github/workflows/deploy.yml) - CI/CD pipeline configuration[cite: 223].

---

## ⚙️ Prerequisites & Tech Stack
[cite_start]To maintain the high-performance standards required for modern sports management[cite: 30], the following stack is used:
1. [cite_start]**Python 3.11+**: Core backend language[cite: 43].
2. **CrewAI & LangChain**: Multi-agent orchestration and LLM memory.
3. **Google Gemini API**: Advanced reasoning and report generation.
4. **Serper API**: Real-time web search for live scores and match data.
5. [cite_start]**AWS EC2 (N. Virginia)**: Cloud infrastructure for global accessibility[cite: 48].

---

## 📦 Installation & Local Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kartikdubey96/Sports-Planner.git](https://github.com/Kartikdubey96/Sports-Planner.git)
   cd Sports-Planner