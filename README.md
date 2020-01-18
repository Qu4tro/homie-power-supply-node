# homie-power-supply-node

**homie-power-supply-node** is a Python package that uses homie-spec to provide a homie node implementation that can be used to create Homie-compliant messages from your power supply device.

This package has no dependencies other than **Python >=3.6** and `homie-spec`. 
Only Linux is supported at the moment, as it uses `/sys/class/power_supply/*/uevent` to read the power supply properties.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `homie-power-supply-node`.

```bash
pip install homie-power-supply-node
```

## Usage
```python
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
"""
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
