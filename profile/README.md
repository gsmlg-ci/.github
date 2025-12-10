```
   _____ _____ __  __ _       _____       _____ _____
  / ____|/ ____|  \/  | |     / ____|     / ____|_   _|
 | |  __| (___ | \  / | |    | |  __ ____| |      | |
 | | |_ |\___ \| |\/| | |    | | |_ |____| |      | |
 | |__| |____) | |  | | |____| |__| |    | |____ _| |_
  \_____|_____/|_|  |_|______|\_____|     \_____|_____|

```

## Docker Images

This organization maintains Docker images for various services and tools.

All images are published to:
- **Docker Hub**: `docker.io/gsmlg/{image}`
- **GitHub Container Registry**: `ghcr.io/gsmlg-dev/{image}`

### Image List

<!--START_SECTION:images-->
| Image | Docker Hub | GHCR | Build Status |
|-------|------------|------|--------------|
| [alpine](https://github.com/gsmlg-ci/alpine) | `gsmlg/alpine` | `ghcr.io/gsmlg-dev/alpine` | [![Build](https://github.com/gsmlg-ci/alpine/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/alpine/actions/workflows/build.yml) |
| [antlr](https://github.com/gsmlg-ci/antlr) | `gsmlg/antlr` | `ghcr.io/gsmlg-dev/antlr` | [![Build](https://github.com/gsmlg-ci/antlr/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/antlr/actions/workflows/build.yml) |
| [baidupcs-go](https://github.com/gsmlg-ci/baidupcs-go) | `gsmlg/baidupcs-go` | `ghcr.io/gsmlg-dev/baidupcs-go` | [![Build](https://github.com/gsmlg-ci/baidupcs-go/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/baidupcs-go/actions/workflows/build.yml) |
| [build-base](https://github.com/gsmlg-ci/build-base) | `gsmlg/build-base` | `ghcr.io/gsmlg-dev/build-base` | [![Build](https://github.com/gsmlg-ci/build-base/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/build-base/actions/workflows/build.yml) |
| [caddy](https://github.com/gsmlg-ci/caddy) | `gsmlg/caddy` | `ghcr.io/gsmlg-dev/caddy` | [![Build](https://github.com/gsmlg-ci/caddy/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/caddy/actions/workflows/build.yml) |
| [code-server](https://github.com/gsmlg-ci/code-server) | `gsmlg/code-server` | `ghcr.io/gsmlg-dev/code-server` | [![Build](https://github.com/gsmlg-ci/code-server/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/code-server/actions/workflows/build.yml) |
| [couch-alpine](https://github.com/gsmlg-ci/couch-alpine) | `gsmlg/couch-alpine` | `ghcr.io/gsmlg-dev/couch-alpine` | [![Build](https://github.com/gsmlg-ci/couch-alpine/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/couch-alpine/actions/workflows/build.yml) |
| [couchdb](https://github.com/gsmlg-ci/couchdb) | `gsmlg/couchdb` | `ghcr.io/gsmlg-dev/couchdb` | [![Build](https://github.com/gsmlg-ci/couchdb/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/couchdb/actions/workflows/build.yml) |
| [curl](https://github.com/gsmlg-ci/curl) | `gsmlg/curl` | `ghcr.io/gsmlg-dev/curl` | [![Build](https://github.com/gsmlg-ci/curl/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/curl/actions/workflows/build.yml) |
| [daedalos](https://github.com/gsmlg-ci/daedalos) | `gsmlg/daedalos` | `ghcr.io/gsmlg-dev/daedalos` | [![Build](https://github.com/gsmlg-ci/daedalos/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/daedalos/actions/workflows/build.yml) |
| [dell-openmanage](https://github.com/gsmlg-ci/dell-openmanage) | `gsmlg/dell-openmanage` | `ghcr.io/gsmlg-dev/dell-openmanage` | [![Build](https://github.com/gsmlg-ci/dell-openmanage/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/dell-openmanage/actions/workflows/build.yml) |
| [dell-poweredge](https://github.com/gsmlg-ci/dell-poweredge) | `gsmlg/dell-poweredge` | `ghcr.io/gsmlg-dev/dell-poweredge` | [![Build](https://github.com/gsmlg-ci/dell-poweredge/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/dell-poweredge/actions/workflows/build.yml) |
| [devdocs](https://github.com/gsmlg-ci/devdocs) | `gsmlg/devdocs` | `ghcr.io/gsmlg-dev/devdocs` | [![Build](https://github.com/gsmlg-ci/devdocs/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/devdocs/actions/workflows/build.yml) |
| [echo](https://github.com/gsmlg-ci/echo) | `gsmlg/echo` | `ghcr.io/gsmlg-dev/echo` | [![Build](https://github.com/gsmlg-ci/echo/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/echo/actions/workflows/build.yml) |
| [editor-server](https://github.com/gsmlg-ci/editor-server) | `gsmlg/editor-server` | `ghcr.io/gsmlg-dev/editor-server` | [![Build](https://github.com/gsmlg-ci/editor-server/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/editor-server/actions/workflows/build.yml) |
| [geoip2](https://github.com/gsmlg-ci/geoip2) | `gsmlg/geoip2` | `ghcr.io/gsmlg-dev/geoip2` | [![Build](https://github.com/gsmlg-ci/geoip2/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/geoip2/actions/workflows/build.yml) |
| [go-ethereum](https://github.com/gsmlg-ci/go-ethereum) | `gsmlg/go-ethereum` | `ghcr.io/gsmlg-dev/go-ethereum` | [![Build](https://github.com/gsmlg-ci/go-ethereum/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/go-ethereum/actions/workflows/build.yml) |
| [keycloak](https://github.com/gsmlg-ci/keycloak) | `gsmlg/keycloak` | `ghcr.io/gsmlg-dev/keycloak` | [![Build](https://github.com/gsmlg-ci/keycloak/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/keycloak/actions/workflows/build.yml) |
| [kubectl](https://github.com/gsmlg-ci/kubectl) | `gsmlg/kubectl` | `ghcr.io/gsmlg-dev/kubectl` | [![Build](https://github.com/gsmlg-ci/kubectl/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/kubectl/actions/workflows/build.yml) |
| [log-forwarder](https://github.com/gsmlg-ci/log-forwarder) | `gsmlg/log-forwarder` | `ghcr.io/gsmlg-dev/log-forwarder` | [![Build](https://github.com/gsmlg-ci/log-forwarder/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/log-forwarder/actions/workflows/build.yml) |
| [mariadb](https://github.com/gsmlg-ci/mariadb) | `gsmlg/mariadb` | `ghcr.io/gsmlg-dev/mariadb` | [![Build](https://github.com/gsmlg-ci/mariadb/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/mariadb/actions/workflows/build.yml) |
| [meshcentral](https://github.com/gsmlg-ci/meshcentral) | `gsmlg/meshcentral` | `ghcr.io/gsmlg-dev/meshcentral` | [![Build](https://github.com/gsmlg-ci/meshcentral/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/meshcentral/actions/workflows/build.yml) |
| [nginx](https://github.com/gsmlg-ci/nginx) | `gsmlg/nginx` | `ghcr.io/gsmlg-dev/nginx` | [![Build](https://github.com/gsmlg-ci/nginx/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/nginx/actions/workflows/build.yml) |
| [nix-builder](https://github.com/gsmlg-ci/nix-builder) | `gsmlg/nix-builder` | `ghcr.io/gsmlg-dev/nix-builder` | [![Build](https://github.com/gsmlg-ci/nix-builder/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/nix-builder/actions/workflows/build.yml) |
| [openssl](https://github.com/gsmlg-ci/openssl) | `gsmlg/openssl` | `ghcr.io/gsmlg-dev/openssl` | [![Build](https://github.com/gsmlg-ci/openssl/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/openssl/actions/workflows/build.yml) |
| [openwrt](https://github.com/gsmlg-ci/openwrt) | `gsmlg/openwrt` | `ghcr.io/gsmlg-dev/openwrt` | [![Build](https://github.com/gsmlg-ci/openwrt/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/openwrt/actions/workflows/build.yml) |
| [phoenix](https://github.com/gsmlg-ci/phoenix) | `gsmlg/phoenix` | `ghcr.io/gsmlg-dev/phoenix` | [![Build](https://github.com/gsmlg-ci/phoenix/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/phoenix/actions/workflows/build.yml) |
| [python](https://github.com/gsmlg-ci/python) | `gsmlg/python` | `ghcr.io/gsmlg-dev/python` | [![Build](https://github.com/gsmlg-ci/python/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/python/actions/workflows/build.yml) |
| [rabbitmq](https://github.com/gsmlg-ci/rabbitmq) | `gsmlg/rabbitmq` | `ghcr.io/gsmlg-dev/rabbitmq` | [![Build](https://github.com/gsmlg-ci/rabbitmq/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/rabbitmq/actions/workflows/build.yml) |
| [semantic-release](https://github.com/gsmlg-ci/semantic-release) | `gsmlg/semantic-release` | `ghcr.io/gsmlg-dev/semantic-release` | [![Build](https://github.com/gsmlg-ci/semantic-release/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/semantic-release/actions/workflows/build.yml) |
| [snapdrop](https://github.com/gsmlg-ci/snapdrop) | `gsmlg/snapdrop` | `ghcr.io/gsmlg-dev/snapdrop` | [![Build](https://github.com/gsmlg-ci/snapdrop/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/snapdrop/actions/workflows/build.yml) |
| [squid](https://github.com/gsmlg-ci/squid) | `gsmlg/squid` | `ghcr.io/gsmlg-dev/squid` | [![Build](https://github.com/gsmlg-ci/squid/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/squid/actions/workflows/build.yml) |
| [stunnel](https://github.com/gsmlg-ci/stunnel) | `gsmlg/stunnel` | `ghcr.io/gsmlg-dev/stunnel` | [![Build](https://github.com/gsmlg-ci/stunnel/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/stunnel/actions/workflows/build.yml) |
| [svg-autocrop](https://github.com/gsmlg-ci/svg-autocrop) | `gsmlg/svg-autocrop` | `ghcr.io/gsmlg-dev/svg-autocrop` | [![Build](https://github.com/gsmlg-ci/svg-autocrop/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/svg-autocrop/actions/workflows/build.yml) |
| [tinyproxy](https://github.com/gsmlg-ci/tinyproxy) | `gsmlg/tinyproxy` | `ghcr.io/gsmlg-dev/tinyproxy` | [![Build](https://github.com/gsmlg-ci/tinyproxy/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/tinyproxy/actions/workflows/build.yml) |
| [unbound](https://github.com/gsmlg-ci/unbound) | `gsmlg/unbound` | `ghcr.io/gsmlg-dev/unbound` | [![Build](https://github.com/gsmlg-ci/unbound/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/unbound/actions/workflows/build.yml) |
| [varnish](https://github.com/gsmlg-ci/varnish) | `gsmlg/varnish` | `ghcr.io/gsmlg-dev/varnish` | [![Build](https://github.com/gsmlg-ci/varnish/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/varnish/actions/workflows/build.yml) |
| [zerotier](https://github.com/gsmlg-ci/zerotier) | `gsmlg/zerotier` | `ghcr.io/gsmlg-dev/zerotier` | [![Build](https://github.com/gsmlg-ci/zerotier/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/zerotier/actions/workflows/build.yml) |
| [zerotier-ui](https://github.com/gsmlg-ci/zerotier-ui) | `gsmlg/zerotier-ui` | `ghcr.io/gsmlg-dev/zerotier-ui` | [![Build](https://github.com/gsmlg-ci/zerotier-ui/actions/workflows/build.yml/badge.svg)](https://github.com/gsmlg-ci/zerotier-ui/actions/workflows/build.yml) |
<!--END_SECTION:images-->

### Internal Dependencies

Some images depend on others:

- `alpine` is used by: baidupcs-go, go-ethereum, zerotier
- `curl` is used by: kubectl, geoip2
- `code-server` is used by: editor-server

### Usage

```bash
# Pull from Docker Hub
docker pull gsmlg/{image}:latest

# Pull from GitHub Container Registry
docker pull ghcr.io/gsmlg-dev/{image}:latest
```

### Trigger Builds

To rebuild all images or a specific image, use the [trigger-builds workflow](https://github.com/gsmlg-ci/.github/actions/workflows/trigger-builds.yml).
