from github import Auth, Github
import os

auth = Auth.Token(os.environ["GITHUB_TOKEN"])
github_client = Github(auth=auth)
REPO_NAME = "CodSpeedHQ/Advent"
GITHUB_ADVENT_REPO = github_client.get_repo(REPO_NAME)
