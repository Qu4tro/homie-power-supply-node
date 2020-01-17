"Introduces pytest fixtures that are necessary to run the test suite."

import os
from typing import List
from pathlib import Path

import pytest  # type: ignore

from tests.common import FinalMessage, final_messages


@pytest.fixture(scope="session", autouse=True)
def load_power_supply_directory_env() -> None:
    """
    Load POWER_SUPPLY_DIRECTORY into the tests environment variables.

    This is used to load the files inside `tests/data`
    """
    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
    os.environ["POWER_SUPPLY_DIRECTORY"] = str(dir_path / "tests" / "data")


@pytest.fixture(scope="module", autouse=True)
def power_supply_1_node_messages() -> List[FinalMessage]:
    "Returns the power supply for the uvent file in 1_*"
    return final_messages(1)
