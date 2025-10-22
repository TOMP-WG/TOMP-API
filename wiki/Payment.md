[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Payment](Payment.md)  

The scope of the Payment module is limited to the communication between TOs and MPs concerning settlement and clearing, not about ticketing or the actual payment process.
The payment phase is for now pretty simple: the MP should pay frequently the made trips to the TO. This is not in scope of the API. The only thing we provide is an endpoint, listing the journal-lines for each leg (the fare) or other items to pay (fines, etc.). 

## Overview of journal entries
* Request per period, category or state
* Id 
  - journalId (can be leg id)
  - journalSequenceId (per leg there can be multiple entries, like fare, fines, damages, etc.)
* Invoice and expiration date
* Amount, currency code, tax
* State [TO_INVOICE, INVOICED]
* Some leg info
  - Travelled distance & distance type (km, mile)
  - Travelled time
  - This way the internal consistency can be guaranteed (you can calculate the final price using these properties and the fare object). In some cases the travelled time or distance can be used to work with budgets.
* Bank account (future usage)

See also the [Fare construction](Fare-construction.md)  

### In depth: the fare object
* Fare consists of multiple ‘fare parts’
* Each fare part has:
  - Type (FIXED, FLEX, MAX)
  - Amount
  - Currency code
  - Tax rate 
* And to support relative costs:
  - Units (default 1)
  - Unit type (e.g., hour, minute, kilometre…) 
  - Example: bike rental, 1.50USD per half an hour {type: flex, amount: 1.50, currency-code: USD, units: 0.5, unit-type: hour}
* And to support scales:
  - Scale from (start of scale, if absent 0)
  - Scale to (end of scale, if absent infinity)
  - Scale type (e.g., kilometre, hour)
  - Example: bike rental, 1.50USD per half hour for the first hour, after this 2.50USD per hour: this are 2 fare parts:
{type: flex, amount: 1.50, currency-code: USD, units: 0.5, unit-type: hour, scale-from: 0, scale-to: 1, scale-type: hour
{type: flex, amount: 2.50, currency-code: USD, units: 1, unit-type: hour, scale-from:1, scale-type: hour}

### Claim extra costs
* You have to provide this:
  - Amount
  - Currency code
  - Tax rate
  - Category: [ ALL, DAMAGE, LOSS, STOLEN, EXTRA_USAGE, REFUND, FINE, OTHER_ASSET_USED, CREDIT, VOUCHER, DEPOSIT, OTHER ]
  - Description (Mandatory in case of ‘OTHER’)
  - Account (bank account, future usage)
* What does this facilitate?
  - Deposits (deposit & refund)
  - All kinds of scenarios resulting from trip execution