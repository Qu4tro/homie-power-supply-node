"Test the messages returned by the power supply node"

from functools import partial
from tests.common import all_node_messages, find_message_and_get_payload


def test_power_supply_0() -> None:
    "Test the messages returned by the power supply node"
    messages = all_node_messages(0)

    assert all(m.qos == 1 for m in messages)
    assert all(m.retained is True for m in messages)

    assert messages[0].topic == "device/power-supply/$name"
    assert messages[0].payload == "0_AC"

    assert messages[1].topic == "device/power-supply/$type"
    assert messages[1].payload == "power-supply"

    assert messages[2].topic == "device/power-supply/$properties"
    assert messages[2].payload == "name,online"

    assert messages[3].topic == "device/power-supply/name/$name"
    assert messages[3].payload == "Name"

    assert messages[4].topic == "device/power-supply/name/$datatype"
    assert messages[4].payload == "string"

    assert messages[5].topic == "device/power-supply/online/$name"
    assert messages[5].payload == "Online"

    assert messages[6].topic == "device/power-supply/online/$datatype"
    assert messages[6].payload == "boolean"

    assert messages[7].topic == "device/power-supply/name"
    assert messages[7].payload == "AC"

    assert messages[8].topic == "device/power-supply/online"
    assert messages[8].payload == "false"

    assert len(messages) == 9


def test_power_supply_1_node_attributes() -> None:
    "Test the messages returned by the power supply node"
    messages = all_node_messages(1)

    assert messages[0].topic == "device/power-supply/$name"
    assert messages[0].payload == "1_BAT"

    assert messages[1].topic == "device/power-supply/$type"
    assert messages[1].payload == "power-supply"

    assert messages[2].topic == "device/power-supply/$properties"
    prop_names = ",".join(
        [
            "name",
            "status",
            "present",
            "technology",
            "cycle_count",
            "voltage_min_design",
            "voltage_now",
            "power_now",
            "energy_full_design",
            "energy_full",
            "energy_now",
            "capacity",
            "capacity_level",
            "model_name",
            "manufacturer",
            "serial_number",
        ]
    )
    assert messages[2].payload == prop_names


def test_power_supply_1_prop_gets() -> None:
    "Test the messages returned by the power supply node"
    messages = all_node_messages(1)
    match = partial(find_message_and_get_payload, messages)

    assert match("device/power-supply/name") == "BAT0"
    assert match("device/power-supply/status") == "Discharging"
    assert match("device/power-supply/present") == "1"
    assert match("device/power-supply/technology") == "Li-poly"
    assert match("device/power-supply/cycle_count") == "646"
    assert match("device/power-supply/voltage_min_design") == "11.1"
    assert match("device/power-supply/voltage_now") == "10.928"
    assert match("device/power-supply/power_now") == "7.955"
    assert match("device/power-supply/energy_full_design") == "45.0"
    assert match("device/power-supply/energy_full") == "34.12"
    assert match("device/power-supply/energy_now") == "4.76"
    assert match("device/power-supply/capacity") == "13"
    assert match("device/power-supply/capacity_level") == "Normal"
    assert match("device/power-supply/model_name") == "01AV463"
    assert match("device/power-supply/manufacturer") == "LGC"
    assert match("device/power-supply/serial_number") == "1747"
