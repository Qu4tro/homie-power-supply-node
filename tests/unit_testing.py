"Test the messages returned by the power supply node"

from tests.common import final_messages


def test_power_supply_0() -> None:
    "Test the messages returned by the power supply node"
    messages = final_messages(0)

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

    assert len(messages) == 7


def test_power_supply_1() -> None:
    "Test the messages returned by the power supply node"
    messages = final_messages(1)

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

    assert messages[7].topic == "device/power-supply/status/$format"
    assert messages[7].payload == "Unknown,Full,Discharging,Charging"
