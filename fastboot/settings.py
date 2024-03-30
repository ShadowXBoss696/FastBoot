import pathlib
from typing import Any

# Known Paths
PROJECT_ROOT: pathlib.Path = pathlib.Path(__file__).parents[1]
PROJECT_CONFIG_TOML: pathlib.Path = PROJECT_ROOT / "pyproject.toml"

# Settings:
DEVELOP: bool = PROJECT_CONFIG_TOML.exists()


# Settings Schema

KNOWN_SETTINGS: dict[str, Any] = {
    "port": {},
}


class Config:
    def __init__(
        self,
    ) -> None:
        pass
