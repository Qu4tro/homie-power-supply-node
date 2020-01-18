"Test the messages returned by the power supply node"

import pickle
from typing import List

from tests.common import (
    power_supplies_for_test,
    final_messages,
    FinalMessage,
    load_power_supply_directory_env,
    TEST_DIRECTORY_PATH
)

SNAPSHOTS_PATH = TEST_DIRECTORY_PATH / "snapshots"


def read_snapshot(power_supply_id: int) -> List[FinalMessage]:
    """
    Unpickles the saved snapshot file with
    the messages for a given power supply node
    """
    snapshot_path = SNAPSHOTS_PATH / str(power_supply_id)
    with snapshot_path.open("rb") as snapshot_file:
        snapshot: List[FinalMessage] = pickle.load(snapshot_file)
        return snapshot


def write_snapshot(power_supply_id: int, snapshot: List[FinalMessage]) -> None:
    """
    Unpickles the saved snapshot file with
    the messages for a given power supply node
    """
    snapshot_path = SNAPSHOTS_PATH / str(power_supply_id)
    with snapshot_path.open("wb") as snapshot_file:
        pickle.dump(snapshot, snapshot_file)


def test_snapshots() -> None:
    "Test if snapshots match the messages returned by the node"
    for power_supply_id in power_supplies_for_test():
        try:
            snapshot_messages = read_snapshot(power_supply_id)
            current_messages = final_messages(power_supply_id)
            assert snapshot_messages == current_messages
        except FileNotFoundError:
            assert False, "Snapshots not up to date"


def make_snapshots() -> None:
    """
    Create the snapshots by getting the messages
    from each node, pickling them and saving them to disk.

    Can be called with `make snapshots`
    """
    load_power_supply_directory_env()

    for power_supply_id in power_supplies_for_test():
        current_messages = final_messages(power_supply_id)
        write_snapshot(power_supply_id, current_messages)
