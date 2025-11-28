<span style="display: inline-block; white-space: nowrap;"><a href="../home.md">home</a><details style="display: inline;"><summary><a href="../modules.md">modules</a></summary>
*  [core](core.md)  
*  [offer](offer.md)  
*  [pre-sales](pre-sales.md)  
*  [purchase](purchase.md)  
*  [execution](execution.md)  
*  [support](support.md)  
*  [after-sales](after-sales.md)  
*  [travel-information](travel-information.md)  
*  [customer management](customer-management.md)  
*  [discovery](discovery.md)  
*  [tech](tech.md)  

</details></span>

# discovery module

URLS to comply to OGC, to describe the interface

<h3>GET / -> <a href="../objects/landingPage.md">landingPage</a></h3><div style="margin-left:20px"><i>Landing page</i><br>Gives a (technical & human readable) output describing how this API must be used. If  the parameter f=html is supplied, a human readable page must be responded.

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `f` | query | string |  | The optional f parameter indicates the output format that the server shall provide as part of the response document.  The default format is JSON. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [landingPage](../objects/landingPage.md) | The reponse containing a landing page
</details>
<br></div>
</details>
<h3>GET /api</h3><div style="margin-left:20px"><i>This document</i><br>This document

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `f` | query | string |  | The optional f parameter indicates the output format that the server shall provide as part of the response document.  The default format is JSON. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|

</details>
<br></div>
</details>
<h3>GET /collections -> <a href="../objects/collections.md">collections</a></h3><div style="margin-left:20px"><i>the feature collections in the dataset</i><br>returns a collection of available collection (like offers, packages, legs, support-requests and payments)

<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [collections](../objects/collections.md) | A list of available collections
</details>
<br></div>
</details>
<h3>GET /collections/{collectionId}?collectionId=... -> <a href="../objects/collection.md">collection</a></h3><div style="margin-left:20px"><i>describe the feature collection with id `collectionId`</i><br>a (machine or human) readable description of this collection

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `collectionId` | path | string | ✓ | local identifier of a collection |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [collection](../objects/collection.md) | description of data delivered by this collection
</details>
<br></div>
</details>
<h3>GET /conformance -> <a href="../objects/conformance.md">conformance</a></h3><div style="margin-left:20px"><i>API conformance definition</i><br>A list of all conformance classes specified in a standard that the server conforms to.

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `f` | query | string |  | The optional f parameter indicates the output format that the server shall provide as part of the response document.  The default format is JSON. |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [conformance](../objects/conformance.md) | The URIs of all conformance classes supported by the server.

To support "generic" clients that want to access multiple
OGC API Features implementations - and not "just" a specific
API / server, the server declares the conformance
classes it implements and conforms to.
</details>
<br></div>
</details>
<h3>GET /processes -> <a href="../objects/processList.md">processList</a></h3><div style="margin-left:20px"><i>retrieve the list of available processes</i><br>The list of processes contains a summary of each process the OGC API - Processes offers, including the link to a more detailed description of the process. For more information, see <a href="https://docs.ogc.org/is/18-062/18-062.html#sc_process_list">Section 7.9</a>.

<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [processList](../objects/processList.md) | Information about the available processes
</details>
<br></div>
</details>
<h3>GET /processes/{processID}?processID=... -> <a href="../objects/process.md">process</a></h3><div style="margin-left:20px"><i>retrieve a process description</i><br>The process description contains information about inputs and outputs and a link to the execution-endpoint for the process. The Core does not mandate the use of a specific process description to specify the interface of a process. That said, the Core requirements class makes the following _recommendation_ implementations SHOULD consider supporting the OGC process description. For more information, see <a href="https://docs.ogc.org/is/18-062/18-062.html#sc_process_description">Section 7.10</a>.

<details><summary><i>Parameters</i></summary>

| Name | In | Type | Required | Description |
|------|-------|------|----------|-------------|
| `processID` | path | string | ✓ |  |
</details>
<details><summary><i>Responses</i></summary>

| Code | Content type | Type | Description |
|------|-------|-------|-------------|
| 200 | application/json | [process](../objects/process.md) | A process description.
</details>
<br></div>
</details>
