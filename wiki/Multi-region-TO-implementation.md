If you are implementing the TOMP API as TO and have many regions where your assets are not allowed to cross, then namespacing the API is recommended.
# Issues with multiple regions
Imagine a bike operator that serves 100 different cities in Europe wanting to ingrate most of the locations using the TOMP API. Planning and booking trips would be possible by keeping regions in mind when filtering f.x. when “to” and “from” parameters are passed to the planning module.
But problems quickly arise f.x. with listing pricing in the operators module. Different countries will have different pricing in different currencies. Also the regions in the module could quickly grow to a long list.
From the point of view of an MP operating across Europe, the MP would probably also want to use the TO’s integrated on a city basis as you would not want to include a TO in a planning request in a city where that TO does not operate, thus wasting server power both on the TO and MP side. The solution is a namespaced approach like seen in GBFS.

# Namespaced approach
By namespacing the different regions the TO solves the multi-region issue. This means that each region will have its own base URL. A TO serving bikes in Copenhagen, Berlin and Amsterdam could choose to serve them at the following URLs:

http://example.to/tomp/copenhagen/
http://example.to/tomp/berlin/
http://example.to/tomp/amsterdam/

Each region can now have unique pricing and different rules defined. The transport operator should try to segment the regions by geographic area, pricing or meta information. This could f.x. be by city.

It is recommended that the TO serves a list of URLs f.x. on Github for making it easier for MPs to identify regions until a more unified discovery solution is in place.
# When not to namespace
This approach should not be used if you are serving trips that can go across regions, f.x. As a train operator serving trips across Europe. 
