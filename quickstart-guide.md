# TOMP-API

## generate a complete TOMP-API.yaml

You can merge all TOMP-yamls into one, to start generating code. Use 'merge-API.ps1' (powershell script) to merge all items.   
If you use `merge-API.ps1` in a powershell, you'll be asked per module to integrate it. The default value is 'N' for each draft module.  
If you use `merge-API.ps1 all`, all modules will be included, except for the 'draft' modules. There will still be a question for each of them (default 'N'). To ignore them, just keep on entering.  
You can also enlist all modules you want to include (the TOMP-API-1-CORE is always included): e.g. `merge-API.ps1 TOMP-API-2-OFFERS.yaml TOMP-API-4-PURCHASE.yaml`.

### old stuff

redocly join .\TOMP-API.yaml .\TOMP-API-DISCOVERY.yaml -o TOMP-total.yaml --without-x-tag-groups  
redocly join TOMP-API.yaml .\TOMP-API-CONTRACT.yaml .\TOMP-API-CUSTOMER.yaml .\TOMP-API-DATASPACES.yaml .\TOMP-API-DISCOVERY.yaml .\TOMP-API-NOTIFY.yaml .\TOMP-API-PAYMENTS.yaml .\TOMP-API-SUPPORT.yaml .\TOMP-API-TECH.yaml -o TOMP-API-total.yaml --without-x-tag-groups