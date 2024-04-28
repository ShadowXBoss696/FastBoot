<p align="center">
  <picture>
    <source srcset="docs/assets/banner-dark.png" media="(prefers-color-scheme: dark)">
    <img alt="FastBoot" src="docs/assets/banner.png">
  </picture>
</p>

<p align="center">
  <em>An HTTP web server, for Python.</em>
</p>

---

[![License](https://img.shields.io/github/license/ShadowXBoss696/FastBoot)](https://github.com/ShadowXBoss696/FastBoot/blob/develop/LICENSE)
[![Contributors](https://img.shields.io/github/contributors/ShadowXBoss696/FastBoot)](https://github.com/ShadowXBoss696/FastBoot/graphs/contributors)
[![Commit Activity](https://img.shields.io/github/commit-activity/m/ShadowXBoss696/FastBoot)](https://github.com/ShadowXBoss696/FastBoot/graphs/commit-activity)
[![Last Commit](https://img.shields.io/github/last-commit/ShadowXBoss696/FastBoot)](https://github.com/ShadowXBoss696/FastBoot/network)

[![Quality Assurance](https://github.com/ShadowXBoss696/FastBoot/actions/workflows/quality-assurance.yml/badge.svg?branch=develop)](https://github.com/ShadowXBoss696/FastBoot/actions/workflows/quality-assurance.yml)
[![Sanity Suite](https://github.com/ShadowXBoss696/FastBoot/actions/workflows/sanity-suite.yml/badge.svg)](https://github.com/ShadowXBoss696/FastBoot/actions/workflows/sanity-suite.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/8bbfbab0e5cd03667256/maintainability)](https://codeclimate.com/github/ShadowXBoss696/FastBoot/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/8bbfbab0e5cd03667256/test_coverage)](https://codeclimate.com/github/ShadowXBoss696/FastBoot/test_coverage)
[![Vulnerabilities](https://snyk.io/test/github/ShadowXBoss696/FastBoot/badge.svg)](https://snyk.io/test/github/ShadowXBoss696/FastBoot)

Documentation: [FastBoot Wiki](https://github.com/ShadowXBoss696/FastBoot/wiki)

---

FastBoot is an HTTP Web Server implementation for Python. It is heavily influenced by two popular open source projects namely [Gunicorn](https://gunicorn.org/) and [Uvicorn](https://www.uvicorn.org/).

This project aims to bring a complete solution which is broadly compatible with various web frameworks, while still being fairly simple for implementation and usage.

Feel free to join us on the GitHub [discussions](https://github.com/ShadowXBoss696/FastBoot/discussions) page.


# Quickstart

FastBoot requires **Python 3.x >= 3.11**.

Install using `pip` from the PyPI:

```shell
$ pip install fastboot
```

Basic usage:

```shell
$ fastboot [OPTIONS] APP_MODULE
```

Where `APP_MODULE` is of the pattern `$(MODULE_NAME):$(VARIABLE_NAME)`. The module name can be a full dotted path. The variable name refers to a WSGI or a ASGI callable that should be found in the specified module.

For Example:

```shell
$ cd example
$ fastboot demo:app
```

# More on WSGI and ASGI?

Most well established Python Web frameworks started out as WSGI-based frameworks.

WSGI applications are a single, synchronous callable that takes a request and returns a response. This doesn’t allow for long-lived connections, like you get with long-poll HTTP or WebSocket connections, which WSGI doesn't support well.

Having an async concurrency model also allows for options such as lightweight background tasks, and can be less of a limiting factor for endpoints that have long periods being blocked on network I/O such as dealing with slow HTTP requests.


# Contributing

See our complete [contributor's guide](CONTRIBUTING.md) for more details.


# License

FastBoot is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
