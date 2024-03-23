import logging
import uuid

import pytest
from _pytest.capture import CaptureFixture

from fastboot.logging import configure_logging


def assert_logging(capsys: CaptureFixture[str], logger: logging.Logger, expected_log_level: int = logging.INFO) -> None:
    """Asserts if logging is working as expected"""

    for level_name, level in logging.getLevelNamesMapping().items():
        # Build message to log
        message_id: str = str(uuid.uuid4())  # to ensure unique log messages during each test
        message: str = f"This is a {level_name} message (msg_id: {message_id})"

        # Try logging
        logger.log(msg=message, level=level)

        # Test message
        console = capsys.readouterr()
        if level >= expected_log_level:
            assert message in console.out
        else:
            assert message not in console.out


# // default log config ------------------------------------------


def test_logging_default(capsys: CaptureFixture[str]) -> None:
    """Tests loggers default configuration"""

    # noinspection PyBroadException
    try:
        # Try configuring default loggers
        configure_logging()
    except Exception:
        pytest.fail("Failed to configure loggers with default logging configuration")

    # Assert logging
    logger = logging.getLogger("fastboot.testing")
    assert_logging(capsys, logger)
