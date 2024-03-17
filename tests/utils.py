import logging
import re
from collections.abc import Generator
from contextlib import contextmanager
from typing import final

from _pytest.logging import LogCaptureHandler
from pytest import fixture

# // --- Local Log Capture Utils -----------------------------------------------------------

_ANSI_ESCAPE_SEQ = re.compile(r"\x1b\[[\d;]+m")


@final
class LocalLogCaptureFixture:
    """Provides access and control of log capturing from a specific logger"""

    def __init__(self):
        self.handler = LogCaptureHandler()

    @contextmanager
    def capture(self, logger: logging.Logger) -> Generator[None, None, None]:
        logger.addHandler(self.handler)
        try:
            yield
        finally:
            logger.removeHandler(self.handler)

    @property
    def text(self) -> str:
        """The formatted log text."""
        return _ANSI_ESCAPE_SEQ.sub("", self.handler.stream.getvalue())

    @property
    def records(self) -> list[logging.LogRecord]:
        """The list of log records."""
        return self.handler.records

    def clear(self) -> None:
        """Reset the list of log records and the captured log text."""
        self.handler.clear()


@fixture
def local_caplog() -> Generator[LocalLogCaptureFixture, None, None]:
    yield LocalLogCaptureFixture()
