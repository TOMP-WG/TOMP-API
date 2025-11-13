[home](home.md) > [modules](modules.md)

# Modules of TOMP-API v2.0

The TOMP-API v2.0 serves as a **holistic operational API** designed to facilitate robust communication between resellers (MaaS Service Providers, or MPs) and mobility providers (Transport Operators, or TOs). The core objective of the API is to cover the complete user journey, utilizing specific profiles for each transportation mode to ensure the integration is understandable and straightforward to implement.

## Core Functionality Overview (API Modules)

The overall process within the TOMP-API is structured into several modules, although not all modes require every module. The most important modules are enlisted below.

[More details](./modules/core.md)

## Offer Module & Pre-sales Module

The Offer Module allows the MP to search for non-binding offers based on the traveler’s needs. The Pre-sales Module, which is layered on top of the Offer Module, is used primarily in contexts involving planned, long-distance, or long-usage trips (like train rides or car rentals). It enables the MP to select one or multiple offers, modify them, and complete them by adding details such as assigning seats, updating traveler information, or including ancillary products.

[Offer module](./modules/offer.md)  
[Pre-sales module](./modules/pre-sales.md)

## Purchase Module

This module facilitates multiple ways to acquire services: purchasing one or multiple offers, purchasing a package assembled via the Pre-sales Module, purchasing a general product (like subscriptions or day cards), or purchasing the immediate use of a specific asset (like a scooter on a map).

### Purchase Confirmation Flavors

Purchases can be:
* **Immediately Confirmed** (allowing rollback without financial penalty during a specified 'cancel window'), 
* **Auto-confirm** (starting in a PENDING state and automatically confirming upon an expiration deadline), or requiring a 
* **2-phase Purchase** (requiring an explicit second step to confirm the pending package).

[More details](./modules/purchase.md)

## Execution Module

This module manages the phase where the traveler is actively consuming the mobility services. This flow is primarily leg-based (a package can contain multiple legs) and encompasses actions initiated by the traveler, such as **starting, ending, pausing, and resuming** the trip segment. Assets and ancillaries can be assigned to a specific leg before it starts.

[More details](./modules/execution.md)

## Support Module

This is necessary to address unusual situations, such as flat tires or other asset-related issues. The Transport Operator (TO) relies on the MP having implemented the notification module, as callbacks are utilized during the support process.

[More details](./modules/support.md)

## After-sales Module (including Payment)

This module handles financial reporting, such as reporting balances or requesting deposits. Crucially, it also contains functionality for addressing 'redress options,' including requesting refunds, compensation, or reimbursement. Payments can be handled upfront, upon completion ("Pay when finished"), or as part of a subscription model.

[More details](./modules/after-sales.md)

# Mode specific functions

The TOMP-API provides functions tailored to the operational requirements of different transport modes.

## 1. Two-wheeled Shared Vehicles (Bikes, Scooters, Steps)

This blueprint is designed for shared services, typically operating in **free-floating or station-based models**. The execution flow is particularly important here because the **traveler is in control** of the vehicle, unlike modes controlled by a human driver.

*   **Execution:** Key execution steps involve the user actively initiating the **starting, ending, pausing, and resuming** of the vehicle/leg. When needed, travelers can also request to **extend the leg** usage time.
*   **Asset Operations:** The API supports specific operations directly on the asset, such as using the `operation-asset` facility to perform actions like **opening a trunk** or, in a custom implementation, using a function like `open-helmet-box/execute`.
*   **Geospatial Data:** During the execution phase, the operator can publish **GeoJSON data** detailing boundaries for free-floating areas, no-go areas, and required (non-)parking zones.
*   **User Communication:** The TO can communicate mandatory operational **instructions** (e.g., for operating a manual lock) using links within the leg details, ensuring the MP shows this information before the next step is executed. **Warnings** or informational messages can also be sent to the traveler using the notification module.
*   **Purchasing:** For these modes, purchase initiation commonly begins in three ways: starting with a vehicle visible on the map (**Asset based**), purchasing an offer obtained via journey planning (**Offer based**), or purchasing supplementary items like subscriptions or day cards (**Product based**).

More details can be found [here](/documents/Blue%20print%20v2%20-%20Bikes%20scooters%20steps.docx).

## 2. Shared Cars

Shared cars blend features from 2-wheeled vehicles and DRT/Taxis. While the vehicle is delivered according to the DRT pattern, the physical usage mimics 2-wheeled modes, as the user initiates actions like starting and stopping the vehicle.

*   **Pre-sales Flexibility:** The offer and pre-sales flows are frequently used. Before or after purchase, customers can **alter or extend offers** by adding ancillary products (like a child’s seat or additional insurance) or adjusting start/end locations and times.
*   **Execution Actions:** The execution module is centered on user control, supporting the functions for **starting, ending, pausing, and resuming** the vehicle/leg.
*   **Direct Asset Manipulation:** Functionality exists to perform direct operations on the car asset, such as **opening a trunk** or unlocking a side door in a garage.
*   **Geospatial and Communication:** The TO can deliver GeoJSON data covering (non-)parking and return areas during execution. Communication of mandatory instructions and traveler warnings is managed via links and the notification module, similar to 2-wheeled vehicles.
*   **Payment Guarantees:** Deposits, acting as a financial guarantee, are a common element in the payment flow, particularly when the MP and TO are unfamiliar with one another.

More details can be found [here](/documents/Blue%20print%20v2%20-%20Shared%20cars.docx).

## 3. DRT & Taxis (Demand Responsive Transport)

This mode deals with rides typically controlled by a human driver. Consequently, the notification process is extremely important for the MP.

*   **Delayed Confirmation:** Unlike shared assets, DRT/Taxi purchases often use the **Delayed Confirmed** flavor. The package starts in a PENDING state until the TO confirms the ride by finalizing planning (e.g., assigning a driver), at which point the TO must use the notification module to update the MP to a CONFIRMED state.
*   **Execution Focus:** The execution flow focuses on critical stages managed by the TO: the vehicle **arriving** at the pick-up location, the passenger **boarding**, and the passenger **alighting**.
*   **Real-Time Updates:** During the PREPARING state, the TO utilizes the notification module to inform the MP of status changes, including **vehicle location updates and Estimated Time of Arrival (ETA) updates**.
*   **Support Scenarios:** A key support scenario addressed is when the user cannot locate the vehicle at the pick-up spot, which the MP can report using the `NOT_AT_LOCATION` support type. The system also handles scenarios where the user **does not show up** (`USER_NO_SHOW`).
*   **Flexible Payment:** Payment methods are versatile, including **Fixed Price Upfront, Estimated Price Upfront, Pay Afterwards (pay as you go)**, and **Batch payments** for accounting multiple trips.

More details can be found [here](/documents/Blue%20print%20v2%20-%20DRT%20%26%20Taxis%201.docx).

## 4. Public Transport (Train, Tram, Bus)

For traditional public transport, the complexity lies in managing offers, products, and tickets, making the pre-sales module particularly relevant, while execution is often less critical.

*   **Pre-sales Tailoring:** The Pre-sales Module is essential for combining and modifying offers (e.g., combining different legs into a single package). This allows for modifications such as **assigning seats**, adding/removing ancillary products, and updating traveler details before the final purchase.
*   **Ticket Management:** The system must handle the retrieval of tickets, or "travel documents". This includes supporting requests for **static tickets** (PDF or image format) and **dynamic tickets** (which change over time for anti-fraud purposes and require the `travel-documents` endpoint for immediate retrieval).
*   **Modern Execution Flows:** Although less frequently used for traditional PT, the Execution Module supports new methods of travel validation, such as initiating a new leg based on the use of a time-limited product or card. This functionality facilitates **Swipe-on/off** and **Be-in/out** scenarios by initiating and ending a leg using the API.
*   **Redress and Refunds:** The After-sales Module offers comprehensive redress options. When something goes wrong, the MP can request options for **exchange, refund (partial or full), or reimbursement**. Proof required for reimbursements can be delivered through the Support Module.
*   **Payment Model:** Upfront payment is standard in a Business-to-Consumer context, often utilizing the **auto-commit flow** where the pending package is confirmed once payment arrives. Subscriptions are common in B2B implementations, requiring the TO to publish financial credit details to the MP.

More details can be found [here](/documents/Blue%20print%20v2%20-%20Public%20Transport.docx).
