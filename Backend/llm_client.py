import os
import json
from typing import Dict, Any, List
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

SYSTEM_PROMPT = """
You are an assistant that analyzes GitHub issues.

Return ONLY a JSON object with exactly these keys:

summary (string)
type (string, one of: "bug", "feature_request", "documentation", "question", "other")
priority_score (string, like "3 - Medium priority")
suggested_labels (list of strings)
potential_impact (string)

Rules:
- NEVER use "enhancement". If enhancement detected, map it to "feature_request".
- priority_score MUST be a string, not a number.
- If number is generated, convert to: "<number> - <text>"
- No explanation, no text outside JSON.
"""

def build_prompt(title: str, body: str, comments: List[str]) -> str:
    comments_text = "\n---\n".join(comments) if comments else "No comments."
    return f"Title:\n{title}\n\nBody:\n{body}\n\nComments:\n{comments_text}"

def analyze_issue_with_llm(title: str, body: str, comments: List[str]) -> Dict[str, Any]:
    prompt = build_prompt(title, body, comments)
    model = genai.GenerativeModel("gemini-2.0-flash")  # works in your env

    response = model.generate_content(SYSTEM_PROMPT + "\n\n" + prompt)
    text = response.text

    start = text.find("{")
    end = text.rfind("}")
    data = json.loads(text[start:end + 1])

    # ---- normalization -----
    valid_types = {"bug", "feature_request", "documentation", "question", "other"}
    if data.get("type") not in valid_types:
        data["type"] = "feature_request"

    priority = data.get("priority_score")
    if isinstance(priority, int):
        data["priority_score"] = f"{priority} - Priority"
    elif not isinstance(priority, str):
        data["priority_score"] = "3 - Priority"

    return data
