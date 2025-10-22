**Q**: What should I implement of the Operator Information module?<br>
**A**: Actually everything. More shared information increases the possibility that your API will be used.<br>
_The operator information normally doesn't need authorization nor authentication._

You can simply create endpoints (tip: generate them with editor.swagger.io. Attach them to a database/file system you have. Deploy the server code to a server, configure the database access and off you go!

The available endpoints are (comparable with GBFS, extended with extra fare information):
* stations 
* regions (just names)
* information (information about the TO, can be extended later on)
* calendar (opening days)
* opening hours 
* pricing plan (extended regarding GFBS, all pricing parts can be described now)
* available assets (returning asset-types & amounts that are available, per location). This should be as realtime as possible!
* alerts

For planning purposes the available-assets **MUST** be implemented. You have to provide more accurate information during the planning phase, calling the planning-options endpoint. 