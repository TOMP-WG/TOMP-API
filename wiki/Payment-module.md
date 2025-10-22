
# Payment module

The scope of the Payment module is limited to the communication between TOs and MPs concerning settlement and clearing, not about ticketing or the actual payment process. The Payment module offers two alternative payment models that can also be used in conjunction: a prepayment model and a post-payment model. A prepayment model can be used to exchange payment information regarding fares for the legs booked, deposit, subscriptions, etc. A post-payment model can be used to exchange payment information after a trip has been completed regarding fares for the legs travelled, reimbursements, fines, etc. Table 7 presents the functions between MPs and TOs within this process, which relate to the User stories presented earlier in §4.

Currently, the payment module supports only reporting and requesting payments. The TO can enlist all the trip costs and ‘other costs’, like fines, extra usages etc. The MP can request the ‘journal items’ to find out how much has to be paid to the TO. In the journal items, there is also a precise description of the executed leg: distance, time etc. All different scenarios (prepaid, postpaid, subscription, deposits, fines, etc) can be implemented with the current setup.


**Functions between MaaS-provider and Transport Operator**

| Category | Function | User Story (See Appendix A.4 )|
|---|---|---|
|Payment/PrePay|Request / receive payment <> Request / receive payment	|1.2; 1.3|
|Payment/PostPay|Request / receive payment <> Request / receive payment	|1.2; 1.3|

_Table 7. Functions between the MPs and TOs within the Payment process_  


In addition, Table 8 describes the transition states that take place during the Payment process. These states are helpful to understand the steps and actions within the process of making a reservation. The booking states are also indicated in the operational flow presented in Fig. 8.

**Payment states**
|#|	State|	Description|
|---|---|---|
|T|To invoice|TO requests payment from MP|
|I|Invoiced|TO has confirmed payment from MP|  

_Table 8. Transition states of the Payment process_  

![Payment module](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki%20F8_Payment.png?raw=true)  
_Fig. 8: Operational view of the Payment module_

In the near future usable clearing houses will be constructed in the ecosystem (by the market). TOs and MPs can use these clearing houses for frequent clearing of the fares and other payments.