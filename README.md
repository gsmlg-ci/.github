# gsmlg-ci Organization

This repository manages the organization profile and provides tools for managing Docker image builds across all repositories in the gsmlg-ci organization.

## Docker Images

All Docker images in this organization are published to:
- Docker Hub: `docker.io/gsmlg/{image}`
- GitHub Container Registry: `ghcr.io/gsmlg-dev/{image}`

See [profile/README.md](profile/README.md) for the complete list of images and their build status.

## Scripts

- `scripts/update_readme.py` - Updates the organization profile with current repository information
- `scripts/trigger_builds.sh` - Triggers builds across all Docker image repositories

## Workflows

- `update-readme.yml` - Runs weekly to update the organization profile
- `trigger-builds.yml` - Manually trigger builds for all or specific images

## Usage

### Trigger All Builds

```bash
gh workflow run trigger-builds.yml --repo gsmlg-ci/.github
```

### Trigger Specific Image Build

```bash
gh workflow run trigger-builds.yml --repo gsmlg-ci/.github -f image=nginx
```

## Related

- [gsmlg-dev/Foundation](https://github.com/gsmlg-dev/Foundation) - Original monorepo (Docker images migrated from here)
