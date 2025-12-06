from pydantic import BaseModel, HttpUrl
from typing import List, Literal

class AnalyzeIssueRequest(BaseModel):
    repo_url: HttpUrl
    issue_number: int

class IssueAnalysisResponse(BaseModel):
    summary: str
    type: Literal["bug", "feature_request", "documentation", "question", "other"]
    priority_score: str  # e.g. "3 - Medium priority, affects one feature but has a workaround."
    suggested_labels: List[str]
    potential_impact: str
