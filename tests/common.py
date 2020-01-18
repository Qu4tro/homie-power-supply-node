"Set of functions that are useful to multiple test cases"

import os
from pathlib import Path
from typing import NamedTuple, List, Iterator

from homie_power_supply_node import PowerSupply


TEST_DIRECTORY_PATH = Path(os.path.dirname(os.path.realpath(__file__)))


class FinalMessage(NamedTuple):
    "Immutable object for a message that is ready to send"
    topic: str
    payload: str
    qos: int
    retained: bool


def all_node_messages(index: int) -> List[FinalMessage]:
    """
    Returns a list of the node messages for the power supply
    instantiated from the uvent file in 0_*
    """
    node = get_power_supply(index).node

    # Let's start with the declarative messages
    messages = list(node.messages(prefix="device/power-supply"))

    if node.properties is not None:
        # Let's add in the get messages for each prop
        messages.extend(
            [
                node.getter_message(prop_name, prefix="device/power-supply")
                for prop_name in node.properties
            ]
        )

    return [
        FinalMessage(m.topic, m.payload, m.qos, m.retained)
        for m in messages
    ]


def get_power_supply(index: int) -> PowerSupply:
    """
    Returns the power supply for the given index

    For a tree like this:
    tests
    ├── data
    │   ├── 0_AC
    │   │   └── uevent
    │   └── 1_BAT

    `get_power_supply(1)` would return the PowerSupply associated with 1_BAT
    """
    for power_supply in PowerSupply.find_all():
        try:
            if int(power_supply.name.split("_")[0]) == index:
                return power_supply
        except ValueError as err:
            raise ValueError("Malformed data directory") from err
    raise ValueError("Index is too high or there's missing test data")


def power_supplies_for_test() -> Iterator[int]:
    "List the indexes of the power supplies in the tests/data directory"
    for power_supply in PowerSupply.find_all():
        yield int(power_supply.name.split("_")[0])


def load_power_supply_directory_env() -> None:
    """
    Load POWER_SUPPLY_DIRECTORY into the process environment variables.

    This is used to load the test files inside `tests/data`
    """
    os.environ["POWER_SUPPLY_DIRECTORY"] = str(TEST_DIRECTORY_PATH / "data")
