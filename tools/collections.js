const collections = [
    {
        "question": "Do you publish available assets in GBFS?",
        "category": "offers",
        "json": [{
            "rel": "[code]:gbfs:vehicle",
            "type": "application/json",
            "href": "[your base url]/gbfs/vehicle_status.json"
        },
        {
            "rel": "[code]:gbfs:station",
            "type": "application/json",
            "href": "[your base url]/gbfs/station_information.json"
        }
        ]
    },
    {
        "question": "Do you publish stops in GTFS?",
        "category": "offers",
        "json": [{
            "rel": "[code]:gtfs:stop",
            "type": "text/csv",
            "href": "[your base url]/gtfs/stops.txt"
        }]
    },
    {
        "question": "Do you publish routes in GTFS?",
        "category": "offers",
        "json": [{
            "rel": "[code]:gtfs:route",
            "type": "text/csv",
            "href": "[your base url]/gtfs/routes.txt"
        }]
    },
    {
        "question": "Is it required to request details of a single offer?",
        "category": "offers",
        "json": [{
            "rel": "offers",
            "href": "[your base url]/tomp/v2/collections/offers/items"
        }]
    },
    {
        "question": "Must package details be retrievable at any time (not only as response)?",
        "category": "execution",
        "json": [{
            "rel": "packages",
            "href": "[your base url]/tomp/v2/collections/packages/items"
        }]
    },
    {
        "question": "Is it required to publish available assets at their location?",
        "category": "pre-sales",
        "json": [{
            "rel": "assets",
            "href": "[your base url]/tomp/v2/collections/assets/items"
        }]
    },
]