<table>
  <tr>
    <th width="80%" style="text-align: left !important;">
      <img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP%20WG%20grey.png" width="300" style="display: inline-block;">
    </th>
    <th width="20%">&nbsp;</th>
  </tr>
  <tr>
    <td style="vertical-align: top;">
      <h1>TOMP-API</h1>
        The Transport Operator to Mobility-as-a-Service Provider API (TOMP-API) is an open standard designed to facilitate seamless technical communication between Transport Operators and Mobility-as-a-Service (MaaS) Providers. Developed and maintained by the TOMP Working Group, the API aims to enhance interoperability within the mobility sector. For more information, visit our
        <a href="https://tomp-wg.org/">homepage</a>.
      <h2>Community and Support</h2>
      <p>Join our community for support and collaboration:</p>
      <ul>
        <li>
          <strong>Slack</strong>: Connect with developers and stakeholders on our
          <a href="https://join.slack.com/t/tomp-wg/shared_invite/zt-2wlthgcar-kHnS4XzAvoWuqnznqcHl~g">Slack channel</a>.
        </li>
        <li>
          <strong>Mailing List</strong>: Contact our secretariat
          (<a href="mailto:TOMP-Secretary@maas-alliance.eu">TOMP-Secretary@maas-alliance.eu</a>)
          to join our mailing list and receive updates on working group meetings.
        </li>
      </ul>
Working group meetings are held monthly to develop and specify the TOMP-API. All reports can be found in our
        <a href="https://github.com/TOMP-WG/TOMP-API/tree/master/documents/working%20group%20reports">meeting repository</a>.

The working group meetings take place every month with the goal to develop and specify a generic TOMP-API for use by Transport Operators and Mobility-as-a-service Providers. All reports can be found at the
        <a href="https://github.com/TOMP-WG/TOMP-API/tree/master/documents/working%20group%20reports">documentation page</a>.

<h2>Getting Started</h2>
<p>To begin implementing TOMP-API:</p>
<ol>
  <li>
    <strong>Documentation</strong>:
    The full version of the API is available on
    <a href="https://app.swaggerhub.com/apis-docs/TOMP-API-WG/transport-operator_maas_provider_api/">SwaggerHub</a>.
  </li>
  <li>
    <strong>Blueprint</strong>:
    We've written new ones for v2, per mode:
    <a href="https://github.com/TOMP-WG/TOMP-API/tree/master/documents">Blue prints v2</a>
  </li>
  <li>
    <strong>Wiki</strong>:
    Explore the
    <a href="/wiki/home.md">TOMP-API Wiki</a>
    for implementation guidance.
  </li>
  <li>
    <strong>our quick start guide</strong>
    <a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/home.md">here</a>
  </li>
  <li>
    <strong>code-snippets</strong>:
    there are some code snippets (mostly Python available to speed up your implementation).
  </li>
  <li>
    <strong>static output</strong>:
    we already prepared all static output from most meta-data endpoints. You can include them directly in your solution.
  </li>
</ol>

<td style="width: 220px;">
<b>Base modules</b>
<ul>
  <li title="Enables requesting offers."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#offer-module--pre-sales-module">Offer</a></li>
  <li title="Facilitates the purchase of (mobility) services."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#purchase-module">Purchase</a></li>
  <li title="Manages the execution phase of the trip."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#execution-module">Execute</a></li>
</ul>
<b>Functional additions</b>
<ul>
  <li title="Allows to reserve an offer and modify it before purchasing it."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#offer-module--pre-sales-module">Pre sales</a></li>
  <li title="Offers customer support functionalities."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#support-module">Support</a></li>
  <li title="Manages after sales processes, like refunding or revokation of tickets."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md#after-sales-module-including-payment.md">After sales</a></li>
</ul>
<b>Supportive modules</b>
<ul>
  <li title="To become OGC compliant, you need to implement these endpoints."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules/discovery.md">Discovery</a></li>
  <li title="Handles user-related information and preferences."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules/customer-management.md">Customer Management</a></li>
  <li title="(draft) data exchange that is not yet standardized yet (like user profiles, license and card types)."><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules/travel-information.md">Information</a></li>
</ul>
<b>Reseller module (MP)</b>
<ul>
  <li title="The part of the API that must be implemented by the reseller/MP, to cope with messages sent by the TO or driver. It contains also confirmation and payment requests.">Notify</li>
</ul>
<b>Per mode</b><br>
<ul><li><a href="https://github.com/TOMP-WG/TOMP-API/blob/master/wiki/modules.md">Details</a></li></ul>

<b>License</b><br>
<a href="http://www.apache.org/licenses/LICENSE-2.0">
  <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License: Apache 2.0">
</a>

<b>Code of conduct</b><br>
<a href="https://github.com/TOMP-WG/TOMP-API/blob/master/code_of_conduct.md"><img src="https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg" alt="Contributor Covenant 2.1 badge"></a>

  </tr>
</table>

<!-- img align="center" src="https://github.com/TOMP-WG/website/blob/master/wiki/images/TOMP%20WG%20grey.png" width="300" -->
