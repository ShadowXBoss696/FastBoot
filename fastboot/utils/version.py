import functools
import importlib.metadata
import pathlib
import tomllib

DEV_SUFFIX: str = "dev"


@functools.cache
def read_version() -> str:
    """
    Extracts the version
    """
    try:
        root_dir = pathlib.Path(__file__).parents[2]
        with open(root_dir / "pyproject.toml", "rb") as pyproject_file:
            return tomllib.load(pyproject_file)["tool"]["poetry"]["version"] + "-" + DEV_SUFFIX
    except FileNotFoundError:
        return importlib.metadata.version(__package__ or __name__.split(".", maxsplit=1)[0])
