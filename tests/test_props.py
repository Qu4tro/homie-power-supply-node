"Test the messages returned by the power supply node"

from tests.common import power_supplies_for_test, all_node_messages, get_power_supply


def test_qos_and_retained() -> None:
    """
    Check if all messages returned by the
    power supply node have QOS 1 and are retained
    """
    for power_supply_id in power_supplies_for_test():
        messages = all_node_messages(power_supply_id)
        assert all(m.qos == 1 for m in messages)
        assert all(m.retained is True for m in messages)


def test_node_attributes() -> None:
    "Test the attribute messages of the given power supply node"

    for power_supply_id in power_supplies_for_test():
        power_supply = get_power_supply(power_supply_id)
        messages = all_node_messages(power_supply_id)

        assert messages[0].topic == "device/power-supply/$name"
        assert messages[0].payload == power_supply.name

        assert messages[1].topic == "device/power-supply/$type"
        assert messages[1].payload == "power-supply"

        assert messages[2].topic == "device/power-supply/$properties"
        assert len(messages[2].payload.split(",")) == len(power_supply.properties())


def test_prop_names() -> None:
    "Check if all the $name attribute messages are correct"
    for power_supply_id in power_supplies_for_test():
        messages = all_node_messages(power_supply_id)
        for message in messages:
            if not message.topic.endswith("$name"):
                continue
            if message.topic == "device/power-supply/$name":
                continue

            assert message.topic.split("/")[-2] == message.payload.lower()


def test_prop_datatypes() -> None:
    "Check if all the $name attribute messages are correct"
    for power_supply_id in power_supplies_for_test():
        messages = all_node_messages(power_supply_id)
        for message in messages:
            if not message.topic.endswith("$datatype"):
                continue

            assert message.payload in ["string", "enum", "integer", "float", "boolean"]
