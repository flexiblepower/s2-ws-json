# S2 JSON

S2 JSON is a translation of the EN50491-12-2 "S2" standard for home and building energy management into JSON schema's for a message based interaction between a Energy Management System (EMS) and an Energy Smart Appliance (ESA).

For more information about S2 visit [s2standard.org](https://s2standard.org/).

This repository contains the JSON schema files for the messages that are being exchanged. It is often used in combination with [S2 Connect](https://github.com/flexiblepower/s2-connect), which specifies how these messages can be exchanged over IP-based networks.

## The S2 standard
S2 Connect is a solution that builds upon two other specification projects. Note that each of these projects could be used on its own.

* **S2 Standard**: The S2 standard, formally known as the European standard EN50491-12-2, defines the data models and interactions between a CEM and RM for energy management.
* **S2 JSON**: Translates the S2 standard into formal JSON schema's for messages that can be exchanged between CEM and RM.
* **S2 Connect**: Protocol specification for discovering, pairing and starting a communication channel for exchanging S2 JSON messages.

The S2 standard is defined in the European standard EN50491-12-2. It is a protocol for managing flexible energy resources (e.g. home batteries, EV chargers, (hybrid) heat pumps, whitegoods, curtailable PV systems) to optimize the power consumption of the building. It defines the protocol between a Customer Energy Manager (CEM) and the Resource Manager (RM).

## Documentation
Documentation for all S2 specification projects can be found on [docs.s2standard.org](https://docs.s2standard.org/).

## JSON Schema
[JSON Schema](https://json-schema.org/) is a common format for defining the structure of JSON messages. An (incomplete) list of code generators can be found [here](https://json-schema.org/implementations.html#code-generation). JSON Schema only defines the messages, but not how they are sent or in which order. 

Inside the `messages` directory schemas can be found for messages that can be sent individually over the WebSocket session. Inside the `schemas` directory schemas can be found that are used within messages, but cannot be send individually.

## Status
The specification is still under development, and currently in beta.

## Discussion
You are welcome to join the discussion on the [S2 Discord server](https://discord.com/invite/NyFMEPmuDw)! For specific feedback to this project you can of course also open issue.

## License
This project is licensed under the Apache License 2.0.
See the LICENSE file for details.