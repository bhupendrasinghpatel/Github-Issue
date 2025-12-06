import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from models import AnalyzeIssueRequest, IssueAnalysisResponse
from github_client import fetch_issue_data
from llm_client import analyze_issue_with_llm

app = FastAPI(
    title="GitHub Issue Assistant",
    description="Analyze a GitHub issue using an LLM and return structured JSON.",
    version="0.1.0",
)

# Allow frontend (we'll call from browser)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; you can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "GitHub Issue Assistant API is running."}


@app.post("/analyze_issue", response_model=IssueAnalysisResponse)
def analyze_issue(payload: AnalyzeIssueRequest):
    # 1. Fetch issue from GitHub
    try:
        title, body, comments = fetch_issue_data(payload.repo_url, payload.issue_number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=502, detail=str(e))

    # 2. Analyze with LLM
    try:
        analysis = analyze_issue_with_llm(title, body, comments)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")

    # 3. Validate and return as Pydantic model
    try:
        return IssueAnalysisResponse(**analysis)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"LLM output not in expected format: {e}. Output was: {analysis}",
        )
