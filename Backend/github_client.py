import re
import os
from typing import Tuple, List
import requests


def parse_repo_url(repo_url: str) -> Tuple[str, str]:
    """
    Extract owner and repo from URL, e.g.
    https://github.com/facebook/react -> ("facebook", "react")
    """
    pattern = r"github\.com/([^/]+)/([^/]+)"
    match = re.search(pattern, repo_url)
    if not match:
        raise ValueError("Invalid GitHub repository URL.")
    owner = match.group(1)
    repo = match.group(2).replace(".git", "")
    return owner, repo


def get_github_headers() -> dict:
    token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def fetch_issue_data(repo_url, issue_number: int) -> tuple[str, str, list[str]]:
    """
    Returns (title, body, comments) for the given issue.
    repo_url may be a HttpUrl object; convert to str.
    """
    repo_url_str = str(repo_url)
    owner, repo = parse_repo_url(repo_url_str)
    base = "https://api.github.com"
    issue_url = f"{base}/repos/{owner}/{repo}/issues/{issue_number}"

    resp = requests.get(issue_url, headers=get_github_headers())
    if resp.status_code == 401:
        resp = requests.get(issue_url, headers={"Accept": "application/vnd.github+json"})

    if resp.status_code != 200:
        raise RuntimeError(f"GitHub API error: {resp.status_code} {resp.text}")

    issue_json = resp.json()
    title = issue_json.get("title", "") or ""
    body = issue_json.get("body", "") or ""

    comments_url = issue_json.get("comments_url")
    comments: List[str] = []
    if comments_url:
        c_resp = requests.get(comments_url, headers=get_github_headers())
        if c_resp.status_code == 401:
            c_resp = requests.get(comments_url, headers={"Accept": "application/vnd.github+json"})
        if c_resp.status_code == 200:
            for c in c_resp.json():
                comments.append(c.get("body", "") or "")

    return title, body, comments
