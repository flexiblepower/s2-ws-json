# s2-ws-json
A WebSockets and JSON based protocol specification implementing the EN50491-12-2 "S2" standard for home and building energy management

## Status
This protocol specification is still under development and not yet stable. It is being developed as part of the Dutch [GO-e project](https://www.tno.nl/nl/duurzaam/systeemtransitie/toekomstbestendige-energienetten/flexibel-elektriciteitsnet/).

Feedback on this protocol specification is very much welcome! Please open an issue.

## S2 protocol
The S2 protocol is defined in the European standard EN50491-12-2. It is a protocol for managing flexible energy resources (e.g. home batteries, EV chargers, (hybrid) heat pumps, whitegoods, curtailable PV systems) to optimize the power consumption of the building. It defines the protocol between a Customer Energy Manager (CEM) and the Resource Manager (RM). For more details visit the website of the [Flexiblepower Alliance Network (FAN)](https://flexible-energy.eu/).

S2 is designed to support different protocol implementations, which are all compatible. This protocol implementation is designed for use on IP-based networks such as a LAN or the Internet, but can also be used for communication between modules running on the same machine.

## Specification
This specification is intended to be used for generating stub and skeleton code for implementing the protocol in different programming languages. Tooling for generating code varies per programming language. In order to cover as many code generation tools as possible, this repository contains two formats for formally specifying the messages used in the protocol: AsyncAPI and JSON Schema. Code generated form either of these two formats should be compatible with each other.

### AsyncAPI
A protocol specification in the [AsyncAPI](https://www.asyncapi.com/) file format. The specification can easily be viewed using the [AsyncAPI Studio](https://studio.asyncapi.com/). Although AsyncAPI supports many transport protocols, we currently limit communication to WebSockets. Information regarding the official generator can be found [here](https://www.asyncapi.com/tools/generator).

For convenience, there are several files which can be used in different situations. S2 defines multiple ControlTypes, which are sub-protocols defining how a certain form of flexibility can be described and controlled. A CEM typically implements all ControlTypes. However, a Resource Manager typically only implements one. In order to make the specification files smaller and more clear, there are also files for the Resource Managers that only support one control type.

* **s2-cem.yaml:** For a CEM, contains all ControlTypes
* **s2-rm.yaml:** For a Resource Manager, contains all ControlTypes
* **s2-rm-ddbc-only.yaml:** For a Resource Manager, contains only the Demand Driven Based Control (DDBC) ControlType
* **s2-rm-frbc-only.yaml:** For a Resource Manager, contains only the Fill Rate Based Control (FRBC) ControlType
* **s2-rm-ombc-only.yaml:** For a Resource Manager, contains only the Operation Mode Based Control (OMBC) ControlType
* **s2-rm-pebc-only.yaml:** For a Resource Manager, contains only the Power Envelope Based Control (PEBC) ControlType
* **s2-rm-ppbc-only.yaml:** For a Resource Manager, contains only the Power Profile Based Control (PPBC) ControlType

### JSON Schema
[JSON Schema](https://json-schema.org/) is a common format for defining the structure of JSON messages. An (incomplete) list of code generators can be found [here](https://json-schema.org/implementations.html#code-generation). JSON Schema only defines the messages, but not how they are sent or in which order. 

Inside the `messages` directory schemas can be found for messages that can be sent individually over the WebSocket session. Inside the `schemas` directory schemas can be found that are used within messages, but cannot be send indiviually.

### Schemas in OpenAPI format
**NB**: s2-ws-json is not a REST API and thus cannot be specified in OpenAPI!

Since s2-ws-json doesn't use REST but WebSockets, OpenAPI is not a good fit and cannot be used to generate s2-ws-json endpoints. However, in some situations the code generator for OpenAPI are of better quality than those for AsyncAPI or JSON-Schema. As a practical solution, for such situations an OpenAPI specification with the schemas for s2-ws-json is provided as well. When using this file to generate code, programmers need to remove or ignore all code related to normal HTTP requests, and implement a WebSocket connection themselves.

## Documentation
Further documentation regarding the s2-ws-json protocol specification can be found on the [GitHub Wiki](https://github.com/flexiblepower/s2-ws-json/wiki).
