The fare can be constructed out of multiple items. The fare communicated from TO to MSP is the fare the TO will be charging the MSP. How the MSP will charge it to the end user, is up to the MSP.

## Fare
The fare consists of a serie of 'fare-parts'. Each part has it's own type. <br>
The first and simplest part is the fixed price (e.g. 12.50 EUR). <br>
_{ "amount": 12.50, "currency-code": "EUR", "tax-rate": 21.0, "type": "FIXED" }_<br><br>
Another possibility is a price per time unit (e.g. 1.50 EUR per hour or 0.25 NNK per quarter of an hour) <br>
_{ "amount": 1.50, "currency-code": "EUR", "tax-rate": 21.0, "type": "FLEX", "unit-type": "HOUR", "units": 1 }_<br>
_{ "amount": 0.25, "currency-code": "NNK", "tax-rate": 6.0, "type": "FLEX", "unit-type": "HOUR", "units": 0.25 }_<br><br>
And, of course, there are mixed possibilities (e.g. 1.50 USD start up costs and 0.50 USD per each half hour) <br>
_[{ "amount": 1.50, "currency-code": "USD", "tax-rate": 2.0, "type": "FIXED" },_<br>
_{ "amount": 0.50, "currency-code": "USD", "tax-rate": 6.0, "type": "FLEX", "unit-type": "HOUR", "units": 0.5 }]_<br><br>

All these possibilities are possible in the fare construction. There is no other way of getting the total amount of fare than by processing all fare parts to avoid inconsistency.

## Scales

The scale construct uses has 2 properties `scaleFrom` and `scaleTo`. The `scaleFrom` is inclusive, the `scaleTo` is inclusive as well. 

```json
"fare": {
              "class": "FARE",
              "parts": [
                {
                  "amount": 0.01,
                  "currencyCode": "EUR",
                  "vatRate": 21,
                  "vatCountryCode": "NL",
                  "type": "FLEX",
                  "unitType": "MINUTE",
                  "units": 1,
                  "scaleFrom": 0,
                  "scaleTo": 59,
                  "scaleType": "MINUTE",
                  "class": "FARE"
                }
              ]
            }
```
This means we'll have to pay EUR 0.01 (incl. VAT) per minute, for the first 60 minutes of the ride. Another part should describe the other minutes, so it should start with 60.