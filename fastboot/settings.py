import os
import pathlib
from abc import ABCMeta
from collections.abc import Callable
from typing import Any, Final

PROJECT_ROOT: pathlib.Path = pathlib.Path(__file__).parents[1]
PROJECT_CONFIG_TOML: pathlib.Path = PROJECT_ROOT / "pyproject.toml"

DEVELOP: bool = PROJECT_CONFIG_TOML.exists()

# ---------------------------------------------------------------------------------

PREF_DEF_REGISTRY: list[type["Preference"]] = []


class AppPreferences:

    def __init__(self):
        self._store = {}

        # Initialize store
        for pref in PREF_DEF_REGISTRY:
            pref_obj: Preference = pref()
            self._store[pref_obj.name] = pref_obj

    def __getattr__(self, name: str) -> Any:
        if name not in self._store:
            raise AttributeError(f"No such configuration defined with name '{name}'.")
        return self._store[name].get_value()

    def __setattr__(self, name: str, value: Any) -> None:
        if name != "_store" and name in self._store:
            self._store[name].set_value(value)
        else:
            super().__setattr__(name, value)

    def __str__(self) -> str:
        lines = []
        kmax: int = max(len(k) for k in self._store)
        vmax: int = 30

        for key in self._store:
            value = self._store[key].get_value()
            if callable(value):
                value = f"<{value.__qualname__}()>"
            value_str = str(value)
            if len(value_str) > vmax:
                value_str = value_str[: vmax - 3] + "..."
            lines.append(f"{key:{kmax}}: {value_str}")

        return os.linesep.join(lines)

    __repr__ = __str__


class Preference(metaclass=ABCMeta):
    """
    This class represents the definition of a preference to be loaded by the application.
    """

    name: str
    desc: str
    default: Any = None
    validator: Callable[[Any], None] = None

    # Inner properties
    _value: Any = None

    REQUIRED_ATTRS: Final[list[str]] = ["name", "desc"]

    def __init__(self) -> None:
        # Update the value with the default value
        if self.default is not None:
            self.set_value(self.default)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Check for required attributes
        for attr_key in cls.REQUIRED_ATTRS:
            if not hasattr(cls, attr_key):
                raise TypeError(f"Attribute '{attr_key}' missing for class {cls.__name__}")

        # Wrap validator with staticmethod annotation
        if cls.validator:
            cls.validator = staticmethod(cls.validator)

        # Register the settings
        PREF_DEF_REGISTRY.append(cls)

    def get_value(self) -> Any:
        return self._value

    def set_value(self, value: Any) -> None:
        if self.validator:
            self.validator(value)
        self._value = value

    def __repr__(self):
        return f"<{self.__class__.__name__} object at {id(self):x} with value '{self._value}'>"


# ---------------------------------------------------------------------------------

#
# === For Demo Only ===
#
# class WorkerCount(Preference):
#
#     name = "worker"
#     default = 1
#     desc = """\
#         The number of worker processes for handling requests.
#
#         A positive integer generally in the ``2-4 x $(NUM_CORES)`` range.
#         You'll want to vary this a bit to find the best for your particular
#         application's work load.
#
#         By default, the value of the ``WEB_CONCURRENCY`` environment variable,
#         which is set by some Platform-as-a-Service providers such as Heroku. If
#         it is not defined, the default is ``1``.
#         """
