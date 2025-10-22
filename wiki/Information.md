[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Operator information](Operator-information.md) > [Information](Information.md)  

The information endpoint contains a lot of general information about the TO (or MP). If the TO operates in multiple regions, but the regions don't share this information, it might be wise to implement the TOMP API multiple times with different base urls.
| field | required | description |
| --- | :----- | :------ |
| systemId | * | identifier for this transport system. This should be globally unique (even between different systems). This Id should be provided by the eco system |
| language | * | array of supported languages. All requests in this API contain a header field (`Content-Language`) requesting a response in a certain language. Specify here the allowed languages |
| name | * | Full name of the system to be displayed to customers, match Content-Language |
| shortName | | Optional abbreviation for a system |
| operator | | Name of the operator of the system, match Content-Language |
| url | | The URL of the transport operator. The value must be a fully qualified URL that includes http:// or https://, and any special characters in the URL must be correctly escaped. |
| purchaseUrl | | A fully qualified URL where a customer can purchase a membership or learn more about purchasing memberships |
| startDate | | start date of the TO |
| phoneNumber | | A single voice telephone number for the specified system. This field is a string value that presents the telephone number as typical for the system's service area. It can and should contain punctuation marks to group the digits of the number. |
| email | | A single contact email address for customers to address questions about the system |
| timezone | * | The time zone where the system is located. Time zone names never contain the space character but may contain an underscore. Please refer to the "TZ" value in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones for a list of valid values |
| licenseUrl | | A fully qualified URL of a page that defines the license terms for the GBFS data for this system, as well as any other license terms the system would like to define (including the use of corporate trademarks, etc) |
| typeOfSystem | | Describes the type of system: FREE_FLOATING, STATION_BASED, VIRTUAL_STATION_BASED |
| chamberOfCommerceInfo	| | Information about the Chamber Of Commerce, containing number and registration city |
| conditions | | Added to include possibility to communicatie general rental conditions like minimum age, max. reservation time etc. [amended] |
| productType | | The type of product offered:  RENTAL, SHARING, PARKING, CHARGING | 
| assetClasses | | The types of modalities the TO offers: AIR, BUS, TROLLEYBUS, TRAM, COACH, RAIL, INTERCITYRAIL, URBANRAIL, METRO, WATER, CABLEWAY, FUNICULAR, TAXI, SELFDRIVE, FOOT, BICYCLE, MOTORCYCLE, CAR, SHUTTLE, OTHER, PARKING, MOPED, STEP. This will later on be extended (WORKING_AT_HOME, HOTEL, etc). |
| discoveryUriAndroid| | Uri to detect if the app is available at the mobile. Since 1.1.0: Compliancy GBFS 1.1* |
| discoveryUriIOS | | Uri to detect if the app is available at the mobile. Since 1.1.0: Compliancy GBFS 1.1* |
| storeUriAndroid | | Uri to the Play store. Since 1.1.0: Compliancy GBFS 1.1* |
| storeUriIOS | | Uri to the App Store. Since 1.1.0: Compliancy GBFS 1.1* | 
| feedContactEmail | | A single contact email address for consumers of this feed to report technical issues. Since 1.1.0: Compliancy GBFS 1.1* |   

See * [GBFS 1.1](https://github.com/NABSA/gbfs/blob/v2.0/gbfs.md#system_informationjson)