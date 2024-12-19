<img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP%20WG%20grey.png" width="300">

# TOMP-API

The Transport Operator to Mobility-as-a-Service Provider API (TOMP-API) is an open standard designed to facilitate seamless technical communication between Transport Operators and Mobility-as-a-Service (MaaS) Providers. Developed and maintained by the TOMP Working Group, the API aims to enhance interoperability within the mobility sector. For more information, visit our [homepage](https://tomp-wg.org/).

## Overview

TOMP-API is structured into several functional modules and extensions, each addressing a specific aspect of the interaction between Transport Operators and MaaS Providers:

CORE Modules:

1. **Offer**: Enables requesting offers, based on external sources.
2. **Purchase**: Facilitates the purchase of (mobility) services.
3. **Execute**: Manages the execution phase of the trip.

Extensions:

1. **Pay**: Shows payment details for the services.
2. **Support**: Offers customer support functionalities.
3. **Customer Management**: Handles user-related information and preferences (draft). 
4. **Modify offers**: Allows to reserve an offer and modify it before purchasing it (draft).
5. **After sales**: Manages after sales processes, like refunding or revokation of tickets (draft).
6. **Contract**: Manages the process of contracting on the fly (draft).
7. **Discover & Data spaces**: technical part of the API, easing the technical integration into eco-systems (draft).

MP Module:

1. **Notify**: the part of the API that must be implemented by the reseller/MP, to cope with messages sent by the TO or driver.

<img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP-structure.png">

These modules work together to provide a comprehensive framework for MaaS integration.

## Recent Updates

The latest release of TOMP-API, version 2.0, introduces several enhancements. The 2 major enhancements are:

- **OGC**: Compliancy to the OGC Features standard, making it simple to use output of the API in apps or other (test) tooling.
- **Enhanced Interoperability**: Improved integration with other standards such as NeTEx, GTFS, APDS, and GBFS by complying to Transmodel.

These updates aim to improve user experience and broaden the applicability of the API across various transport modes.

## Getting Started

To begin implementing TOMP-API:

1. **Documentation**: The latest version of the API is available on [SwaggerHub](https://app.swaggerhub.com/apis-docs/TOMP-API-WG/transport-operator_maas_provider_api/).
2. **Blueprint**: Refer to the [Blueprint for a TOMP-API](https://github.com/TOMP-WG/TOMP-API/tree/master/documents) for detailed insights.
3. **Wiki**: Explore the [TOMP-API Wiki](https://github.com/TOMP-WG/TOMP-API/wiki/) for implementation guidance.

## Community and Support

Join our community for support and collaboration:

- **Slack**: Connect with developers and stakeholders on our [Slack channel](https://join.slack.com/t/tomp-wg/shared_invite/zt-2wlthgcar-kHnS4XzAvoWuqnznqcHl~g).
- **Mailing List**: Contact our secretariat (TOMP-Secretary@maas-alliance.eu) to join our mailing list and receive updates on working group meetings.

Working group meetings are held monthly to develop and specify the TOMP-API. All reports can be found in our [meeting repository](https://github.com/TOMP-WG/TOMP-API/tree/master/documents/working%20group%20reports).

## License

This project is licensed under the Apache-2.0 License.

