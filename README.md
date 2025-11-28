<img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP%20WG%20grey.png" width="300">

# TOMP-API

The Transport Operator to Mobility-as-a-Service Provider API (TOMP-API) is an open standard designed to facilitate seamless technical communication between Transport Operators and Mobility-as-a-Service (MaaS) Providers. Developed and maintained by the TOMP Working Group, the API aims to enhance interoperability within the mobility sector. For more information, visit our [homepage](https://tomp-wg.org/).

## Overview

TOMP-API is structured into several functional modules and extensions, each addressing a specific aspect of the interaction between Transport Operators and MaaS Providers:

## Code of conduct
[Our code of conduct](https://github.com/TOMP-WG/TOMP-API/blob/master/code_of_conduct.md) [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

## Community and Support

Join our community for support and collaboration:

- **Slack**: Connect with developers and stakeholders on our [Slack channel](https://join.slack.com/t/tomp-wg/shared_invite/zt-2wlthgcar-kHnS4XzAvoWuqnznqcHl~g).
- **Mailing List**: Contact our secretariat (TOMP-Secretary@maas-alliance.eu) to join our mailing list and receive updates on working group meetings.

Working group meetings are held monthly to develop and specify the TOMP-API. All reports can be found in our [meeting repository](https://github.com/TOMP-WG/TOMP-API/tree/master/documents/working%20group%20reports).

The working group meetings take place every month with the goal to develop and specify a generic TOMP-API for use by Transport Operators and Mobility-as-a-service Providers. All reports can be found at the [documentation page](https://github.com/TOMP-WG/TOMP-API/tree/master/documents/working%20group%20reports).

## The TOMP-API in a glance:

CORE Modules:

1. **Offer**: Enables requesting offers.
2. **Purchase**: Facilitates the purchase of (mobility) services.
3. **Execute**: Manages the execution phase of the trip.

Functional extensions:

1. **Pre sales**: Allows to reserve an offer and modify it before purchasing it.
2. **Support**: Offers customer support functionalities.
3. **After sales**: Manages after sales processes, like refunding or revokation of tickets

Additional supportive extensions:

1. **Discovery**: to become OGC compliant, you need to implement these endpoints.
2. **Customer Management**: Handles user-related information and preferences. 
(draft).
3. **Information**: data exhange that is not yet standardized yet (like user profiles, license and card types).

MP Module:

1. **Notify**: the part of the API that must be implemented by the reseller/MP, to cope with messages sent by the TO or driver. It contains also confirmation and payment requests.

These modules work together to provide a comprehensive framework for MaaS integration.

## Recent Updates

The latest release of TOMP-API, version 2.0, introduces several enhancements. The 2 major enhancements are:

- **OGC**: Compliancy to the OGC Features standard, making it simple to use output of the API in apps or other (test) tooling.
- **Enhanced Interoperability**: Improved integration with other standards such as NeTEx, GTFS, APDS, and GBFS by complying to Transmodel.

These updates aim to improve user experience and broaden the applicability of the API across various transport modes.

## Getting Started

To begin implementing TOMP-API:

1. **Documentation**: The full version of the API is available on [SwaggerHub](https://app.swaggerhub.com/apis-docs/TOMP-API-WG/transport-operator_maas_provider_api/). 
2. **Blueprint**: We've written new ones for v2, per mode: [Blue prints v2](https://github.com/TOMP-WG/TOMP-API/tree/master/documents)
3. **Wiki**: Explore the [TOMP-API Wiki](/wiki/home.md) for implementation guidance.
4. **our quick start guide**
4. **code-snippets**: there are some code snippets (mostly Python available to speed up your implementation).
5. **static output**: we already prepared all static output from some meta-data endpoints. You can include it directly in your solution.

## License

This project is licensed under the Apache-2.0 License.

<img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP%20WG%20grey.png" width="300">
