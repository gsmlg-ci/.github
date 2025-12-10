#!/bin/bash
# Trigger builds for Docker image repositories in gsmlg-ci organization
# Usage: ./trigger_builds.sh [image_name]
# If image_name is provided, only trigger that image. Otherwise trigger all.

set -e

ORG="gsmlg-ci"

# All Docker image repositories
IMAGES=(
  alpine antlr baidupcs-go build-base caddy code-server
  couch-alpine couchdb curl daedalos dell-openmanage dell-poweredge
  devdocs echo editor-server geoip2 go-ethereum keycloak
  kubectl log-forwarder mariadb meshcentral nginx nix-builder
  openssl openwrt phoenix python rabbitmq semantic-release
  snapdrop squid stunnel svg-autocrop tinyproxy unbound
  varnish zerotier zerotier-ui
)

# Images that support workflow_dispatch (can be triggered manually)
DISPATCHABLE=(
  alpine antlr caddy code-server phoenix
)

trigger_build() {
  local image=$1
  echo "Triggering build for $image..."

  # Check if image supports workflow_dispatch
  if [[ " ${DISPATCHABLE[*]} " =~ " ${image} " ]]; then
    if gh workflow run build.yml --repo "${ORG}/${image}" 2>/dev/null; then
      echo "  Triggered via workflow_dispatch"
      return 0
    fi
  fi

  # Try to rerun the last failed workflow
  local run_id
  run_id=$(gh run list --repo "${ORG}/${image}" --limit 1 --json databaseId,conclusion --jq '.[0] | select(.conclusion == "failure") | .databaseId' 2>/dev/null)

  if [ -n "$run_id" ]; then
    if gh run rerun "$run_id" --repo "${ORG}/${image}" 2>/dev/null; then
      echo "  Reran failed workflow $run_id"
      return 0
    fi
  fi

  # If no failed workflow, create an empty commit to trigger push workflow
  echo "  No dispatchable workflow, skipping (push to repo to trigger)"
  return 0
}

# Main logic
if [ -n "$1" ]; then
  # Trigger specific image
  if [[ " ${IMAGES[*]} " =~ " $1 " ]]; then
    trigger_build "$1"
  else
    echo "Error: Unknown image '$1'"
    echo "Available images: ${IMAGES[*]}"
    exit 1
  fi
else
  # Trigger all images
  echo "Triggering builds for all ${#IMAGES[@]} images..."
  echo ""

  for image in "${IMAGES[@]}"; do
    trigger_build "$image"
  done

  echo ""
  echo "Done! Check build status at: https://github.com/orgs/${ORG}/actions"
fi
