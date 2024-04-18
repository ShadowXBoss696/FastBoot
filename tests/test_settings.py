import pytest

from fastboot.settings import PREF_DEF_REGISTRY, AppPreferences, Preference

# ---------------------------
# Module Level Setup/TearDown
# ---------------------------


def setup_module(module) -> None:
    """Setup any state specific to the execution of the given module."""

    # Define dummy validators

    def text_is_not_empty(value: str) -> None:
        """Assert that the given string is not empty."""

        # Assert value is string
        if not isinstance(value, str):
            raise TypeError(f"Invalid value type passed. Expected: 'str', Found: '{value.__class__.__name__}'")

        # Assert value is not empty
        if len(value.strip()) == 0:
            raise ValueError("Empty string passed")

    # Define dummy preferences
    class DummyPreference(Preference):
        name = "dummy_pref"
        desc = """\
            This is a dummy preference for testing purposes.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et
            dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
            fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
            mollit anim id est laborum.
            """
        default = "default_value"
        validator = text_is_not_empty


def teardown_module(module):
    """teardown any state that was previously setup with a setup_module method."""

    # Remove dummy registered preferences
    PREF_DEF_REGISTRY[:] = [pref for pref in PREF_DEF_REGISTRY if pref.__class__.__name__ not in ["DummyPreference"]]


@pytest.fixture
def preferences() -> AppPreferences:
    yield AppPreferences()


def test_prefs_are_registered() -> None:
    """Test if the preferences are registered properly or not"""

    # At least one preference must be registered
    assert len(PREF_DEF_REGISTRY) > 0, "No preference registered"


def test_app_preference_getter_and_setters(preferences: AppPreferences):
    """Test if getting and setting preference is properly working or not."""

    # Test default value
    assert (
        preferences.dummy_pref == "default_value"
    ), f"Default value mismatch. Expected: 'default_value', Found: {preferences.dummy_pref}"

    # Test setting and getting new value
    preferences.dummy_pref = "new_value"

    assert (
        preferences.dummy_pref == "new_value"
    ), f"New value mismatch. Expected: 'new_value', Found: {preferences.dummy_pref}"


def test_print_app_preference(preferences: AppPreferences) -> None:
    """Test app preference values are printed correctly."""

    output: str = repr(preferences)
    print(output)

    assert len(output) > 0, "No output printed"
    assert "dummy_pref" in output, "Dummy preference value is not printed correctly"
