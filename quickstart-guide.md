# TOMP-API

## generate a complete TOMP-API.yaml

You can merge all TOMP-yamls into one, to start generating code. Use 'merge-API.ps1' (powershell script) to merge all items.   
If you use `merge-API.ps1` in a powershell, you'll be asked per module to integrate it. The default value is 'N' for each draft module.  
If you use `merge-API.ps1 all`, all modules will be included, except for the 'draft' modules. There will still be a question for each of them (default 'N'). To ignore them, just keep on entering.  
You can also enlist all modules you want to include (the TOMP-API-1-CORE is always included): e.g. `merge-API.ps1 TOMP-API-2-OFFERS.yaml TOMP-API-4-PURCHASE.yaml`.

The second step is to make the API tailor made to your needs, removing the endpoints you don't need. You have to start the tool 'filter_endpoints' (Python required).

You can watch the video here: https://youtu.be/PI16GUQmIDs
