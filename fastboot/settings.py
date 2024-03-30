import pathlib
from typing import Any

PROJECT_DIR: pathlib.Path = pathlib.Path(__file__).parents[1]

KNOWN_SETTINGS: dict[str, Any] = {
    "port": {},
}


class Config:
    def __init__(
        self,
    ) -> None:
        pass
