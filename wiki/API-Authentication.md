# API Authentication

The TOMP-WG is currently exploring different forms of authentication, the final standard has **not** been decided yet.

Fig. 3 below shows that the API features authentication for each call to allow secure communication and exchange of information between MPs and TOs.


![Authentication](https://github.com/TOMP-WG/website/blob/master/wiki/images/Wiki_F3_API_calls_authentication.png?raw=true)
_Fig. 3: API calls and authentication_

MaaS Provider authentication and authorization should take place following the process below:
* Authorization code – The most common flow, mostly used for server-side and mobile web applications. This flow is similar to how users sign up into a web application using their Facebook or Google account.
* Resource owner password credentials (or just password) – Requires logging in with a username and password. Since in that case the credentials will be a part of the request, this flow is suitable only for trusted clients (for example, official applications released by the API provider).

A Transport Operator might require authentication to communicate with a MaaS Provider,
for example to manage (update/cancel) a booking or to send a call-back request. That makes bidirectional authentication necessary.
