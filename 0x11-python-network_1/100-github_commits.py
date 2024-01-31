#!/usr/bin/python3
"""
A script that takes in a repository name and owner name, sends a GET request
to the GitHub API, and prints the most recent 10 commits with their authors.
"""

import requests
import sys


def get_github_commits(repo, owner):
    # Define the GitHub API endpoint for commits
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    # Send a GET request to retrieve commits
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        commits = response.json()

        # Print the most recent 10 commits
        for i in range(min(10, len(commits))):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")

    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    # Get the repository and owner names from command line arguments
    repo_arg = sys.argv[1]
    owner_arg = sys.argv[2]

    # Call the function with the provided repository and owner names
    get_github_commits(repo_arg, owner_arg)
