import importlib.metadata
import tomllib

from fastboot.globals import PROJECT_DIR

__all__ = []

# Project Information
__author__ = ["Arpan Mahanty <arpan.mahanty.007@gmail.com>"]
__license__ = "MIT"

try:
    # Read version from pyproject file during development
    with open(PROJECT_DIR / "pyproject.toml", mode="rb") as pyproject_file:
        __version__: str = tomllib.load(pyproject_file)["tool"]["poetry"]["version"]

except FileNotFoundError:
    # Read from the package metadata
    __version__: str = importlib.metadata.version(__package__ or __name__.split(".", maxsplit=1)[0])
