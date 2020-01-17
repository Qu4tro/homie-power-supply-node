"Module docstring"

from homie_power_supply_node import __version__


def test_version() -> None:
    "Test version"
    assert __version__ == "0.1.0"
