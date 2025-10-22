[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Personal requirements](Personal-requirements.md)

Since version 1.3.0, it is possible to specify, besides the [requirements](https://github.com/TOMP-WG/TOMP-API/blob/master/documents/CROW%20passenger%20characteristics%20V2.0.xlsx) for less abled people, items you can bring along. Like luggage or bikes.  

These items are also specified in the `CROW passenger characteristics` document.
```
"requirements": {
      "abilities": [ ... ],
      "bringAlong": [
        {
          "source": "https://github.com/TOMP-WG/TOMP-API/blob/master/documents/CROW%20passenger%20characteristics%20V2.0.xlsx",
          "category": "TA",
          "number": "01"
        }
      ]
    },
```