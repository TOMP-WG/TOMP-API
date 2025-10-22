[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Map based](Map-based.md)  

If a TO wants to facilitate MPs in placing assets on a map, the MP can access the /operator/available-assets endpoint, but the TO has to supply the [process identifier](ProcessIdentifiers.md) ASSET_BASED in combination with the EXACT_ID process identifier.  

The TO has to fill the 'assets' field in the [Available assets](Available-assets.md), but has to use rotating IDs to make it hard to track assets (GDPR compliancy). The MP can plan a specific asset on the map, by using the assetId in the POST plannings (see also [Asset based](Asset-based.md)) in the 'useAssets' field.  

The rest of the process is again the same as [Planning based](Planning-based.md).