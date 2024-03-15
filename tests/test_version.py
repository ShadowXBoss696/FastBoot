import fastboot


def test_version_info() -> None:
    assert fastboot.__version__ is not None
