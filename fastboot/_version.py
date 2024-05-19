#  Copyright (c) 2024 Arpan Mahanty
#
#  This file is part of FastBoot released under the MIT license.
#  See the LICENSE for more information.
#
#  This file is part of FastBoot released under the MIT license.
#  See the LICENSE for more information.
#
#  This file is part of FastBoot released under the MIT license.
#  See the LICENSE for more information.

import importlib.metadata
import pathlib
import tomllib

__version__: str

# /// Internal logic -----------------------------------------------------------------------------

_build_script: pathlib.Path = pathlib.Path(__file__).parents[1] / "pyproject.toml"

if _build_script.exists():
    # We know we are running in development mode, as we have found the pyproject.toml file
    __version__ = tomllib.loads(_build_script.read_text())["tool"]["poetry"]["version"] + ".dev"

else:
    # Load metadata from installed package information
    _pkg_name: str = __package__ or __name__.split(".", maxsplit=1)[0]
    __version__ = importlib.metadata.version(_pkg_name)
