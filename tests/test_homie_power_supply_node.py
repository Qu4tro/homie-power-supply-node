"Assert multiple properties related to the test suite itself."

import os

from homie_power_supply_node import PowerSupply


def test_env() -> None:
    "Confirm our session fixture is loading"
    assert "POWER_SUPPLY_DIRECTORY" in os.environ


def test_power_supply_find_all() -> None:
    "Assert that the `data` directory is structured as expected"
    list_found_power_supplies = list(PowerSupply.find_all())

    # Keep increasing for each example added
    assert len(list_found_power_supplies) == 2

    # Assert test data structure.
    for power_supply in list_found_power_supplies:
        # If any of the below fail, a directory name on tests/data needs fixing
        # So the tree should be something like this:
        # tests
        # ├── data
        # │   ├── 0_AC
        # │   │   └── uevent
        # │   └── 1_BAT
        # │       └── uevent
        #
        # Each directory inside data should start with a number and
        # be separated by a underscore.

        assert len(power_supply.name.split("_")) == 2
        assert power_supply.name.split("_")[0].isdigit()
