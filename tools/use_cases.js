const use_cases = [{
    'id': 'O1',
    'question': 'I use GBFS to publish my available assets and stations',
    'category': 'Offer',
    'datasources': [{
        "rel": "[code]:gbfs:vehicle",
        "type": "application/json",
        "href": "[your base url]/gbfs/vehicle_status.json"
    },
    {
        "rel": "[code]:gbfs:vehicle_type",
        "type": "application/json",
        "href": "[your base url]/gbfs/vehicle_type.json"
    },
    {
        "rel": "[code]:gbfs:station",
        "type": "application/json",
        "href": "[your base url]/gbfs/station_information.json"
    }],
    'collections': [],
    'processes': [],
    'process-specs': []
},
{
    'id': 'O2',
    'question': 'I want to publish my offers, and use my existing website or app to book and use them (deep-link)',
    'category': 'Offer',
    'datasources': [],
    'collections': [],
    'processes': [{
        'title': 'Search for offers - deep linking',
        'description': 'Resellers can search for offers and receive a list of available offers with details. The reseller can then redirect the end-user to the my website or app to complete the booking and payment process.',
        'id': 'searchOffers_post',
        'version': '2.0',
        'jobControlOptions': ['sync'],
        'links': [
            { 'rel': 'process-desc', 
              'href': '[your base url]/api#searchOffers', 
              'type': 'application/yaml',
              'description': 'Each feature in the response represents an offer, containing at least one deep-link, with possible types \'rental_uris.web\', \'rental_uris.andriod\' or \'rental_uris.ios\'',
            },
            { 'rel': 'process-desc', 
              'href': '[your base url]/processes/search-offers', 
              'type': 'application/json',
              'description': 'Each feature in the response represents an offer, containing at least one deep-link, with possible types \'rental_uris.web\', \'rental_uris.andriod\' or \'rental_uris.ios\'',
            },
            { 'rel': 'process', 
              'href': '[your base url]/processes/search-offers/execute'
            }
        ]
    }]
},
];