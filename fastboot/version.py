import importlib.metadata
import tomllib
from typing import Any

from fastboot.settings import DEVELOP, PROJECT_CONFIG_TOML


def read_version_from_pyproject() -> str:
    """Reads version string from the pyproject file located at the project root. Mostly used during development only."""

    with open(PROJECT_CONFIG_TOML, mode="rb") as f:
        pyproject: dict[str, Any] = tomllib.load(f)

    return pyproject["tool"]["poetry"]["version"]


def read_version_from_package_metadata() -> str:  # pragma: no cover
    """Reads version string from the package metadata for the current project."""

    pkg_name: str = __package__ or __name__.split(".", maxsplit=1)[0]
    return importlib.metadata.version(pkg_name)


# Version Information
VERSION: str = read_version_from_pyproject() if DEVELOP else read_version_from_package_metadata()
