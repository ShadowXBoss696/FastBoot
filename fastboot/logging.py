from logging.config import dictConfig, fileConfig
from typing import Any

# Define default logging configuration
DEFAULT_LOGGING_CONFIG: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"default": {"()": "logging.Formatter", "fmt": "%(levelname)-8s: %(message)s"}},
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {"fastboot": {"handlers": ["default"], "level": "INFO", "propagate": False}},
}


def configure_logging(config: dict[str, Any] | str | None = None) -> None:
    """
    Configures python loggers for the current process.
    """

    # load default config first
    dictConfig(DEFAULT_LOGGING_CONFIG)

    # load the given config
    if config:  # pragma: no cover
        if isinstance(config, dict):
            # Read the logging configuration from a dictionary.
            dictConfig(config)

        elif config.endswith(".json"):
            # Read the logging configuration from a JSON file.
            jsonConfig(config)

        elif config.endswith((".yaml", ".yml")):
            # Read the logging configuration from a YAML file.
            yamlConfig(config)

        else:
            # Read the logging configuration from a ConfigParser-format file.
            fileConfig(config, disable_existing_loggers=False)


# noinspection PyPep8Naming
def jsonConfig(filePath: str) -> None:
    """Reads the logging configuration from a JSON file"""

    import json

    with open(filePath) as f:
        loaded_config: dict[str, Any] = json.load(f)
        dictConfig(loaded_config)


# noinspection PyPep8Naming
def yamlConfig(filePath: str) -> None:
    """Reads the logging configuration from a YAML file"""

    import yaml

    with open(filePath) as f:
        loaded_config: dict[str, Any] = yaml.safe_load(f)
        dictConfig(loaded_config)
