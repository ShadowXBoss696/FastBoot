import logging

import pytest

from fastboot.logging import configure_logging

from .utils import LocalLogCaptureFixture

LOGGER_NAME: str = "fastboot.testing"
TEST_MESSAGE: str = "This is a default test message."

LOG_ENABLED_FOR: dict[int, bool] = {
    logging.DEBUG: False,
    logging.INFO: True,
    logging.WARN: True,
    logging.ERROR: True,
    logging.FATAL: True,
}


def test_configure_logging_default(local_caplog) -> None:
    """Tests loggers default configuration"""

    # noinspection PyBroadException
    try:
        # Try configuring default loggers
        configure_logging()
    except Exception:
        pytest.fail("Failed to configure loggers with default logging configuration")

    # Assert logging
    assert_logging(local_caplog)


def assert_logging(local_caplog: LocalLogCaptureFixture) -> None:
    # Asserts if logging is working as expected

    logger = logging.getLogger(LOGGER_NAME)

    # Start capturing logs
    with local_caplog.capture(logger):
        for level, should_log in LOG_ENABLED_FOR.items():
            # Clear any existing logs
            local_caplog.clear()

            # Try logging
            logger.log(msg=TEST_MESSAGE, level=level)

            # Test message
            if should_log:
                assert TEST_MESSAGE in local_caplog.text
            else:
                assert TEST_MESSAGE not in local_caplog.text
