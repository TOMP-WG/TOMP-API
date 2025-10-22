
# Process Flows

Together with the eMaaS project team from the University of Twente, process flows for the customer journey have been defined. This helps to scope the necessary functions required in the API building blocks. The goal is to accommodate different business models and variations of transportation within these functional flows. Asset information can be shared for both free-floating systems (bike sharing, car sharing, ride sharing, taxi) and (virtual)station- or fixed-route- based systems (public transport, (virtual)mobility hubs, or station-based transportation) through the functional descriptions provided in this chapter.

### Functional Blocks
The TOMP-API is composed of 8 functional blocks. Fig. 2 below aims at giving a general overview of the different functional modules within the TOMP-API.

![Functional blocks of the TOMP API](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki_F2%20functional%20blocks.png?raw=true)  
_Fig. 2: Functional blocks of the TOMP-API_

The different functions for the interface between MPs and TOs are described as follows: 

* **Operator Information / General Information**: Gives static information on the operator according to the General Bikeshare Feed Specification+ (GBFS+) standard.
* **Privacy and Registration**: Although the focus of the TOMP-API is not on this block because it impacts not only TOs and MPs but the complete MaaS ecosystem, it is included here as a future point for investigation and possible integration in this API.
* **Planning**: Gives information about availability, estimated travel time and costs.
*  **Booking**: Allows reservation of specific assets for a specific place, time and date.
* **Trip Execution**: Allows access to the asset(s) and travel during the booked period.
* **Payment**: Allows settlement between TOs and MPs. Supports different business models (i.e., pay-as-you-go or subscription-based).
* **Support**: Assists users in the solution of operational troubles encountered during any part of the process. Connects with optional support modules.
* **Asset Information**: Is defined as a separate module that can be used by other modules to supplement API calls with specific asset information where applicable. Assets can be vehicles or for example infrastructural assets.
* **Optional modules**: The more dynamic functional blocks have additional optional modules which are used for the execution of sub-processes derived from the main functions which might not be desired or required depending on the scope of the MaaS implementation and Business Models.
