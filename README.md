# 🐙 GitHub Issue Assistant 🔍🤖

## 🌟 Overview

The GitHub Issue Assistant is an AI-driven tool designed to analyze GitHub issues and generate structured insights that help developers and maintainers quickly understand issue context, priority, and impact.

Just provide a GitHub repository URL and an issue number, and the system will analyze the issue using LLM intelligence (Gemini) and return a clean JSON output with:

- 🎯 Issue summary
- 🏷️ Suggested labels
- 🧭 Issue type classification
- 📌 Priority score
- ⚠️ Potential user impact

The project includes a simple UI built using HTML, CSS & JavaScript, and a FastAPI backend for data processing and AI calls.

## 🚀 Features

- 🐙 Analyze issues from any public GitHub repository
- 🧠 AI-powered natural language understanding
- 🏷️ Suggested labels based on issue context
- 📊 Priority scoring
- ⚡ Fast API backend using FastAPI
- 🌐 Clean web UI to interact with the API
- 📦 Returns JSON formatted response for automation

## 🛠️ Tech Stack

### 🎨 Frontend
- HTML5
- CSS3
- JavaScript

### ⚙️ Backend
- FastAPI (Python)
- Pydantic for validation

### 🤖 AI Engine
- Google Gemini LLM

### 🔗 External APIs
- GitHub REST API

> **Note:** No database is required — all data is fetched live from GitHub during analysis.

## 📂 Architecture

### 🔧 Workflow

1. User input → GitHub URL + Issue number
2. Backend fetches issue details from GitHub API
3. LLM analyzes:
   - Title
   - Issue description
   - Comments
4. AI Response → Clean JSON with insights
5. Frontend displays the result neatly

## 🔍 Expected Output

Example JSON:

```json
{
  "summary": "Tests fail due to module caching issue in PhantomJS.",
  "type": "bug",
  "priority_score": "3 - Medium priority, impacts core testing flow.",
  "suggested_labels": ["testing", "cache", "phantomjs"],
  "potential_impact": "Users face unreliable test results on core modules."
}
```

## 🧠 AI Prompt Strategy

The system sends a structured prompt to the LLM divided into:

1. Issue Title
2. Issue Description
3. Issue Comments

Then requests a strict JSON output without extra text to ensure reliability.

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/GitHub-Issue-Assistant.git
cd GitHub-Issue-Assistant
```

### 2️⃣ Backend Setup (FastAPI)

Create and activate virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

Install requirements:

```bash
pip install -r requirements.txt
```

Set your Google Gemini API key:

```bash
export GOOGLE_API_KEY="YOUR_KEY"
```

Run server:

```bash
uvicorn main:app --reload
```

The API docs will be available at:  
👉 http://localhost:8000/docs

### 3️⃣ Frontend Setup (HTML + JS)

Simply open:

```bash
frontend/index.html
```

Or run using Live Server in VS Code.

## 🖥️ Screenshots

### 🌐 Input Form
(Enter repo URL & issue number)

*Add your screenshots here*

### 📦 JSON Output
(Clean structured analysis)

*Add your screenshots here*

## ▶️ Usage

1. Enter GitHub repo URL e.g. `https://github.com/facebook/react`
2. Enter Issue number e.g. `12345`
3. Click **Analyze**
4. View AI-generated JSON output
5. You can copy or download the output for automation

## 🌱 Future Enhancements

- 🚀 Multi-issue batch analysis
- 🤝 Auto-label using GitHub API
- 💬 Add comments summarization
- 🔄 GitHub Actions integration
- 📱 Responsive UI
- 📊 Impact scoring using historical project patterns

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, create a branch, make improvements, and submit a pull request.

## 🙌 Acknowledgements

Thanks to:

- GitHub REST API
- Google Gemini
- FastAPI Community

## ⭐ Support

If you like this project, star the repository ⭐ and share with developers!

---

**Made with ❤️ by developers, for developers**
