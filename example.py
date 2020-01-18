# pylint: skip-file

from homie_spec import Device
from homie_power_supply_node import PowerSupply

desktop = Device(
    id="desktop",
    name="Desktop Computer",
    nodes={"battery": PowerSupply("BAT0").node(whitelist_properties=["capacity"])},
)

messages = desktop.messages()
assert next(messages).topic == "homie/desktop/$state"
assert next(messages).topic == "homie/desktop/$name"
assert next(messages).topic == "homie/desktop/$homie"
assert next(messages).topic == "homie/desktop/$implementation"
assert next(messages).topic == "homie/desktop/$nodes"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/$name"
assert msg.payload == "BAT0"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/$type"
assert msg.payload == "power-supply"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/$properties"
assert msg.payload == "capacity"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/capacity/$name"
assert msg.payload == "Capacity"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/capacity/$datatype"
assert msg.payload == "integer"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/capacity/$unit"
assert msg.payload == "%"

msg = next(messages)
assert msg.topic == "homie/desktop/battery/capacity/$format"
assert msg.payload == "0:100"


print(
    "Current battery capacity: "
    f"{format(desktop.getter_message('battery/capacity').payload)}%"
)
