import re

from fastboot import __version__ as version

SEMANTIC_VERSION_REGEX: re.Pattern[str] = re.compile(
    "^([0-9]+)\\.([0-9]+)\\.([0-9]+)(?:-([0-9A-Za-z-]+(?:\\.[0-9A-Za-z-]+)*))?(?:\\+[0-9A-Za-z-]+)?$"
)


def test_version_info_available() -> None:
    # Checks if the version string is defined
    assert version is not None, "Missing application version information"


def test_version_info_follows_semantic_version_spec() -> None:
    # Checks if the version string follows semantic versioning
    follows_semver_spec: bool = SEMANTIC_VERSION_REGEX.match(version) is not None
    assert follows_semver_spec, "Application version number does not follow the semantic version specification"
