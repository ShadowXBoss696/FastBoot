import re

import fastboot

SEMANTIC_VERSION_REGEX = re.compile(
    "^([0-9]+)\\.([0-9]+)\\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*))?(?:\\+[0-9A-Za-z-]+)?$"
)


def test_version_info_present() -> None:
    assert fastboot.__version__ is not None, "Missing application version information"


def test_version_info_follows_semantic_version_spec() -> None:
    assert SEMANTIC_VERSION_REGEX.match(
        fastboot.__version__
    ), "Application version number does not follow the semantic version specification"
