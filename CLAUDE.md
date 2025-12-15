# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is the `.github` repository for the gsmlg-ci organization. It manages:
- Organization profile (displayed on github.com/gsmlg-ci)
- Automation for triggering Docker image builds across 38+ repositories
- Auto-updating the profile README with current repository information

## Commands

### Trigger Docker Builds

```bash
# Trigger all image builds
gh workflow run trigger-builds.yml --repo gsmlg-ci/.github

# Trigger specific image build
gh workflow run trigger-builds.yml --repo gsmlg-ci/.github -f image=nginx

# Rerun failed builds only
gh workflow run trigger-builds.yml --repo gsmlg-ci/.github -f rerun_failed=true
```

### Update Profile README

```bash
# Run locally (requires GITHUB_TOKEN or GH_TOKEN env var)
pip install requests
python scripts/update_readme.py
```

### Local Script Usage

```bash
# Trigger builds locally (requires gh CLI authenticated)
./scripts/trigger_builds.sh           # all images
./scripts/trigger_builds.sh nginx     # specific image
```

## Architecture

### Workflows

- **trigger-builds.yml**: Manual dispatch workflow to trigger `build.yml` in individual image repos. Uses `TRIGGER_TOKEN` secret for cross-repo access.
- **update-readme.yml**: Runs weekly (Sunday midnight) or on push. Fetches all org repos via GitHub API and regenerates the image table in `profile/README.md`.

### Scripts

- **scripts/trigger_builds.sh**: Bash script with hardcoded list of all Docker image repos. Attempts `workflow_dispatch` first, falls back to rerunning failed workflows.
- **scripts/update_readme.py**: Python script that fetches repos from GitHub API and updates the `<!--START_SECTION:images-->` block in `profile/README.md`.

### Profile

- **profile/README.md**: Organization profile displayed on GitHub. Contains auto-generated table of all Docker images with build status badges. The table between `<!--START_SECTION:images-->` markers is auto-updated.

## Docker Image Registry

All images are published to two registries:
- Docker Hub: `docker.io/gsmlg/{image}`
- GitHub Container Registry: `ghcr.io/gsmlg-dev/{image}`

## Adding New Images

When adding a new Docker image repository to the organization:
1. Add the image name to the `IMAGES` array in both `scripts/trigger_builds.sh` and `.github/workflows/trigger-builds.yml`
2. If the repo supports `workflow_dispatch`, also add it to the `DISPATCHABLE` array in `trigger_builds.sh`
3. The profile README will auto-update on the next weekly run or manual trigger
