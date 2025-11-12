```json
{
    "inputs": {
      "type": "search_offer",
      "specification": {
        "from": "GPS:6.169639,52.253279",
        "to": "local:p2",
        "startTime": "2025-04-24T08:39:01.160Z",
        "endTime": "2025-04-25T08:39:01.160Z"
      },
      "travellers": [
        {
          "type": "traveller",
          "id": "traveller1",
          "entitlements": [
            {
              "id": "string",
              "type": "card_type",
              "cardType": "DISCOUNT",
              "subType": "NL daluren",
            },
          ],
          "requirements": {
            "mode": "TRAIN",
            "class": "FIRST_CLASS",
          }
        }
      ],
      "places": [
        {
          "placeId": "local:p2",
          "addressLine1": "Startline 1",
          "addressLine2": "Discountcity",
        }
      ]
    }
  }
```

