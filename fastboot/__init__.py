import importlib.metadata
import tomllib

__all__ = ["__version__"]

# Project Information
__author__ = ["Arpan Mahanty <arpan.mahanty.007@gmail.com>"]
__license__ = "MIT"

try:
    from fastboot.config import PROJECT_DIR

    # Read version from pyproject file during development
    with open(PROJECT_DIR / "pyproject.toml", mode="rb") as pyproject_file:
        __version__: str = tomllib.load(pyproject_file)["tool"]["poetry"]["version"]

except FileNotFoundError:  # pragma: no cover
    # Read from the package metadata
    __version__: str = importlib.metadata.version(__package__ or __name__.split(".", maxsplit=1)[0])
