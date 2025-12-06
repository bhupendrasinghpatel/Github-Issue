🐙 GitHub Issue Assistant — AI-Powered Issue Analysis 🔍🤖
🚀 Overview

The GitHub Issue Assistant is an intelligent tool that analyzes issues from any GitHub repository using AI (Gemini / OpenAI), and generates a structured JSON report with:

🎯 Issue summary

🏷️ Relevant labels

📌 Issue type

🧠 Priority score

⚠️ Potential impact

It helps developers, maintainers, and open-source contributors quickly triage issues and understand their importance.

The project combines:

💻 FastAPI backend

🧠 LLM for intelligent analysis

🌐 Frontend (HTML + CSS + JS) for clean UX

🎨 Features

🔗 Analyze any GitHub issue using repo URL + issue number

🧠 AI-powered analysis using LLM (Gemini/OpenAI)

📊 Structured JSON output

🏷️ Label suggestions

⚠️ Impact estimation

💡 User-friendly frontend

🌍 REST API for integration

🛠️ Tech Stack
🖥️ Frontend

HTML5

CSS3 (Tailwind optional)

JavaScript

⚙ Backend

FastAPI (Python)

Pydantic data models

🤖 AI / ML

Google Gemini / OpenAI GPT

Prompt Engineering

🔗 External APIs

GitHub REST API

📂 Project Structure
GitHubProject/
│
├─ main.py               # FastAPI
├─ github_client.py      # GitHub fetch logic
├─ llm_client.py         # AI logic
├─ models.py             # Request/response schemas
│
└─ frontend/
   ├─ index.html         # UI
   ├─ style.css
   └─ app.js

🔧 Dataset & Processing

This project does not use a traditional dataset.

Instead, it performs real-time data extraction from GitHub:

🟦 Fetches title / body of issue

💬 Fetches comments

🧹 Prepares a structured prompt

🧠 Sends to LLM for reasoning

📦 Formats output JSON

🧠 AI Model Integration
Flow:

Frontend collects input

Backend calls GitHub API

Data cleaned and merged

AI model (Gemini/GPT) analyzes issue

Returns clean JSON response

Example Output:

{
  "summary": "Test isolation issue in React test environment",
  "type": "feature_request",
  "priority_score": "6 - Medium priority",
  "suggested_labels": ["testing", "isolation"],
  "potential_impact": "Improves test consistency across environments"
}

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/YOUR_USERNAME/GitHub-Issue-Assistant.git
cd GitHub-Issue-Assistant

2️⃣ Backend Setup (FastAPI)
Create venv
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows

Install dependencies
pip install -r requirements.txt

Set environment variable
export GOOGLE_API_KEY="YOUR_KEY"

Run server
uvicorn main:app --reload


Access API at:

http://127.0.0.1:8000/docs

3️⃣ Frontend Setup

Simply open:

frontend/index.html


Or run via VS Code Live Server.

📸 Screenshots
🏠 Home UI

🧠 AI Result View

📦 JSON Output

🧭 Usage

Paste GitHub repo URL

Enter Issue number

Click Analyze

Get instant JSON report

🔮 Future Enhancements

🔁 Analyze multiple issues at once

🏷️ Auto-apply labels using GitHub API

📊 Integrate priority scoring model

🌐 Host backend on cloud (Render/AWS)

📱 Add mobile responsive UI

🤝 Integrate with GitHub Actions

🧠 Fine-tuned custom model

🤝 Contributing

Open-source contributions are welcome.
Feel free to:

Fork the repo

Improve UI/backend

Add features

Submit PRs

