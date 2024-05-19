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

import os
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path


@contextmanager
def working_dir(path: str) -> Generator[None, None, None]:
    """Changes working directory and returns to previous on exit."""
    old_cwd: Path = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_cwd)
