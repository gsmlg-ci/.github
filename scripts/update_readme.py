#!/usr/bin/env python3
"""
Update the organization profile README with current Docker image repository information.
"""

import os
import re
import sys
import requests

ORG = "gsmlg-ci"
README_FILE = "profile/README.md"

def fetch_repos():
    """Fetches a list of Docker image repositories for the organization."""
    repos = []
    url = f"https://api.github.com/orgs/{ORG}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    while url:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        for repo in response.json():
            # Skip the .github repo itself
            if repo["name"] == ".github":
                continue
            if not repo["private"]:
                repos.append({
                    "name": repo["name"],
                    "url": repo["html_url"],
                })

        # Check for next page
        if 'next' in response.links:
            url = response.links['next']['url']
        else:
            url = None

    return sorted(repos, key=lambda x: x["name"])


def generate_image_table(repos):
    """Generates a markdown table for Docker images."""
    table = "| Image | Docker Hub | GHCR | Build Status |\n"
    table += "|-------|------------|------|--------------|\\n"

    for repo in repos:
        name = repo["name"]
        table += f"| [{name}]({repo['url']}) "
        table += f"| `gsmlg/{name}` "
        table += f"| `ghcr.io/gsmlg-dev/{name}` "
        table += f"| [![Build](https://github.com/{ORG}/{name}/actions/workflows/build.yml/badge.svg)](https://github.com/{ORG}/{name}/actions/workflows/build.yml) |\\n"

    return table


def update_readme(table_content):
    """Updates the README file with the new table content."""
    with open(README_FILE, "r") as f:
        content = f.read()

    start_marker = "<!--START_SECTION:images-->"
    end_marker = "<!--END_SECTION:images-->"

    pattern = re.compile(f"{re.escape(start_marker)}.*{re.escape(end_marker)}", re.DOTALL)
    new_content = pattern.sub(f"{start_marker}\\n{table_content}{end_marker}", content)

    with open(README_FILE, "w") as f:
        f.write(new_content)


if __name__ == "__main__":
    try:
        repositories = fetch_repos()
        if not repositories:
            print("No repositories found", file=sys.stderr)
            sys.exit(1)

        markdown_table = generate_image_table(repositories)
        update_readme(markdown_table)
        print(f"Successfully updated {README_FILE} with {len(repositories)} images")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from GitHub API: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
