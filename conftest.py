"Introduces pytest fixtures that are necessary to run the test suite."

import pytest  # type: ignore

from tests.common import load_power_supply_directory_env


@pytest.fixture(scope="session", autouse=True)
def load_env() -> None:
    "Fixtures to load the files inside `tests/data` for all tests"
    load_power_supply_directory_env()
