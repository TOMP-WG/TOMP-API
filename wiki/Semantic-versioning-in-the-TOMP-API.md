[home](https://github.com/TOMP-WG/TOMP-API/wiki) > [Semantic versioning](Semantic-versioning-in-the-TOMP-API.md)   

# Semantic versioning in the TOMP API
Since the 0.6.0 release of the TOMP-API, we use semantic versioning. That means that we uphold the standard that is described on [semver.org](https://semver.org/).

For parties that are implementing TOMP, this means that by looking at our version number, you can quickly identify what has changed and how much work goes into changing your own implementation.

Our version number is defined as follows: MAJOR.MINOR.PATCH
When the MAJOR version updates, there are breaking changes in our API specification.
When the MINOR version updates, functionality is added with backwards compatibilty.
When the PATCH version updates, only backwards compatible bug fixes are introduced.

This means that when TOMP, for instance, goes from 1.2.0 to 1.2.1, you can safely adopt it without too much changes because only a small bug is fixed, the functionality remains the same. When TOMP goes from 1.2.0 to 1.3.0, new functionality is introduced. For instance, we introduced an extra field that describes the amount of fuel a specific modality has, that wasn't there before. When TOMP goes from 1.2.0 to 2.0.0, fields may be changed, objects might be re-orderd, etcetera. This means that you need to take a close look at the exact changes and be prepared more than a few changes in your system are neccessary.