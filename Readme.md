# CemTrak Analytics API
![](./hype-image.jpeg)
### Part of the [CemTrak project](https://github.com/mring33621/CemTrak)
### Open Source Carbon Emissions Tracker
### A [FastAPI](https://fastapi.tiangolo.com/)-based API to Analyze CemTrak Data in [Pandas](https://pandas.pydata.org/) Dataframes

### API Examples:
```
GET localhost:8000/analytics/datadump
[
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Coal Turbine #1",
        "state": "off",
        "measurement_amt": 0.01,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 00:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "NatGas Turbine #2",
        "state": "off",
        "measurement_amt": 0.01,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 00:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Westside Coal Exhaust Scrubber",
        "state": "off",
        "measurement_amt": 0,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 00:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Coal Turbine #1",
        "state": "low",
        "measurement_amt": 0.28,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 09:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Coal Turbine #1",
        "state": "med",
        "measurement_amt": 0.57,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 10:17:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Coal Turbine #1",
        "state": "high",
        "measurement_amt": 0.79,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 12:42:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "NatGas Turbine #2",
        "state": "low",
        "measurement_amt": 0.17,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 13:34:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "NatGas Turbine #2",
        "state": "med",
        "measurement_amt": 0.21,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 16:54:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "NatGas Turbine #2",
        "state": "high",
        "measurement_amt": 0.34,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 17:15:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Westside Coal Exhaust Scrubber",
        "state": "high",
        "measurement_amt": -0.11,
        "measurement_unit": "kt",
        "timestamp": "2024-05-12 23:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Coal Turbine #1",
        "state": "off",
        "measurement_amt": 0.01,
        "measurement_unit": "kt",
        "timestamp": "2024-05-13 00:01:00"
    },
    {
        "organization_name": "HotGas Power Company",
        "emitter_name": "Westside Coal Exhaust Scrubber",
        "state": "off",
        "measurement_amt": 0,
        "measurement_unit": "kt",
        "timestamp": "2024-05-13 03:01:00"
    }
]
```

### Details:
- Not even close to finished...
- Currently depends on services running on the following hardcoded hosts and ports:
  - CemTrak on localhost:8017
  - CemTrak Event Log on localhost:8989