
# Introduction

With Mobility as a Service (MaaS) travellers can plan, book, execute their trips using any available transport mode and pay for all of them via integrated apps. For MaaS to be successful, transport operators are required to share their transport services and availability of their assets in a digital form. To facilitate MaaS providers and thus enable the deployment of MaaS services, transport operators are also required to standardize the digital form to facilitate access to their information. The TOMP-API (Transport Operator to MaaS Provider - Application Programming Interface) is a standardized and technical interface between MaaS providers and transport operators. 

Figure 1 below depicts the concept of having a standard-based Application Programming Interface (API) from Transport Operators (TO) to or from MaaS Providers (MP). It allows all participating companies to communicate about planning, booking, execution, support, general information and payments of multimodal, end-user specific trips. Using the TOMP-API enhances the interoperability between parties in the MaaS ecosystem.


![Fig. 1: The standard-based API for Transport Operators to/from MaaS providers](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki_F1_Standards_based_API.png?raw=true)
_Fig. 1: The standard-based API for Transport Operators to/from MaaS providers_
_(Source: MaaS program of the Dutch Ministry of Infrastructure and Water Management)_
<br/><br/>
## Goal of the blueprint
In this Blueprint for an API for TOs and MPs (the TOMP-API) we look into the necessary functional requirements for the interoperability between transport operators and MaaS Providers. The goal of this document is to:
* Define the necessary scope for full interoperability between TOs for the deployment of MaaS services, always keeping the customer journey in mind to determine which API calls are needed between TOs and MPs.
* Define the necessary parameters and values to fulfil this scope.
* Define the available parameters in various already available APIs and propose amendments where applicable.
<br/><br/>

## Who is involved?
This document has been written to consolidate the work of the Transport Operators and MaaS Providers - Working Group (TOMP-WG). The TOMP-WG is an initiative started in the Netherlands by the _Ministry of Infrastructure and Water Management_ in 2018. The goal of the group is to provide standardised APIs to facilitate the development of the MaaS ecosystem. TOMP is used as standard for the seven MaaS pilots in The Netherlands.  Since 2020 the TOMP-WG has been moved to become an open-source foundation with an international scope. A list with all collaborators, companies and stakeholders involved in the current design and development of the TOMP-API is provided in Appendix A.5
<br/><br/>

## What is in this version?
The first implementations of the TOMP-API took place in the last couple of months which allowed us to improve the API based on the lessons learned. The API is now capable of describing a full MaaS journey. Only minor changes have been added to this Dragonfly version. 

These results are especially reflected in a simplified object model in the planning phase (flattened the object structure of the leg) and a new endpoint with self-describing facilities was created. This last one is needed for (inter)national scale-up, to be informed of what the addressed TO is capable of. 

The digital version of the API is available for consultation at Swaggerhub : https://app.swaggerhub.com/apis/TOMP-API-WG/transport-operator_maas_provider_api/.

