import importlib.metadata
import pathlib
import tomllib


def extract_version() -> str:
    try:
        root_dir = pathlib.Path(__file__).parents[2]
        with open(root_dir / "pyproject.toml", "rb") as pyproject_file:
            version = tomllib.load(pyproject_file)["tool"]["poetry"]["version"]
            return f"{version}-dev"
    except FileNotFoundError:
        return importlib.metadata.version(__package__ or __name__.split(".", maxsplit=1)[0])
