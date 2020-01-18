"Introduces pytest fixtures that are necessary to run the test suite."

from typing import List

import pytest  # type: ignore

from tests.common import FinalMessage, final_messages, load_power_supply_directory_env


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    "Fixtures to load the files inside `tests/data` for all tests"
    load_power_supply_directory_env()


@pytest.fixture(scope="module", autouse=True)
def power_supply_1_node_messages() -> List[FinalMessage]:
    "Returns the power supply for the uvent file in 1_*"
    return final_messages(1)
