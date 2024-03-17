import logging

import pytest
from _pytest.capture import CaptureFixture

from fastboot.logging import configure_logging

LOGGER_NAME: str = "fastboot.testing"
TEST_MESSAGE_FMT: str = "This is a %(levelname)s message."

LOG_ENABLED_FOR: dict[int, bool] = {
    logging.DEBUG: False,
    logging.INFO: True,
    logging.WARN: True,
    logging.ERROR: True,
    logging.FATAL: True,
}


def test_configure_logging_default(capsys: CaptureFixture[str]) -> None:
    """Tests loggers default configuration"""

    # noinspection PyBroadException
    try:
        # Try configuring default loggers
        configure_logging()
    except Exception:
        pytest.fail("Failed to configure loggers with default logging configuration")

    # Assert logging
    assert_logging(capsys)


def assert_logging(capsys: CaptureFixture[str]) -> None:
    # Asserts if logging is working as expected

    logger = logging.getLogger(LOGGER_NAME)

    # Start capturing logs
    for level, should_log in LOG_ENABLED_FOR.items():
        test_msg: str = TEST_MESSAGE_FMT % {"levelname": logging.getLevelName(level).lower()}

        # Try logging
        logger.log(msg=test_msg, level=level)

        # Test message
        console = capsys.readouterr()
        if should_log:
            assert test_msg in console.out
        else:
            assert test_msg not in console.out
