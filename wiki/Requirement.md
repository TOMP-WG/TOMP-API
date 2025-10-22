[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Planning phase](Planning-phase.md) > [Traveler](Traveler.md) > [Requirement](Requirement.md)

The requirement object contains one specified field: "abilities", and can be extended with arbitrary fields (bilateral agreements). The abilities field is an array of 'requirement objects'. These requirement objects facilitate in carrying the data of the Traveler dictionary from CROW.

Example snippet of the Travelers dictionary:

<table style="vertical-align: top;">
<tr><td> Cat </td><td> # </td><td> Name </td><td>  Description </td><td> Type (optional) </td><td> Characteristics </td><td style="width: 200px"> Requirements to be met by the vehicle	</td><td style="width: 200px"> Requirements to be met by the drive </td><td style="width: 200px"> Requirements to be met by the accompanying person </td></tr>
<tr><td> HR </td><td> 01 </td><td> Wheelchair - standard </td><td> Wheelchair in which the passenger remains seated during transport </td><td> "non-electric" and "responsibly secured" </td><td> 1. Meets VVR code<br>2. There are hook symbols on the wheelchair. Note: If these are not on the wheelchair, the municipality must consult with the auxiliary supplier. </td><td> "1. Wheelchair accessible vehicles approved by the RDW after September 2008 shall be (legally mandatory) fitted with standard three-point belts, including in the wheelchair spaces in combination with the restraint system. Normally, all standard three-point belts are based on the fact that a user is always sitting upright". However, standard three-point harnesses can also be dangerous with deviating body postures". </td><td> "1. The driver must be proficient enough to correctly handle the restraint system and the safety belt(s). 2. The driver shall have sufficient time to correctly secure the wheelchair fitted with the restraint system and the wheelchair occupant with a safety belt." </td><td> 1. The personal companion must know what to look out for his own safety.</td></tr>
<tr><td> HR </td><td> 02 </td><td> Wheelchair - electric </td><td> Wheelchair in which the passenger remains seated during transport </td><td> "electric" and "responsibly secured" </td><td> 1. Compliance with VVR code.  2.Maximum width 90 cm. Maximum weight permitted for the ramp and vehicle (For the carrier this may mean excluding the use of ramps and specific vehicles)  </td><td> "1. Wheelchair accessible vehicles approved by the RDW after September 2008 shall be (legally mandatory) fitted with standard three-point belts, including in the wheelchair spaces in combination with the restraint system. Normally, all standard three-point belts are based on the fact that a user is always sits upright"". However, standard three-point harnesses can also be dangerous with deviating body positions.<br>2. The rear entrance to the vehicle must be at least 90 cm wide.                  3. Loading ramps must be suitable for maximum weight""." </td><td> "1. The driver must be proficient enough to correctly handle the restraint system and the safety belt(s). 2. The driver shall have sufficient time to correctly secure the wheelchair fitted with the restraint system and the wheelchair occupant with a safety belt." </td><td> 1. The personal companion must know what to look out for his own safety.</td></tr>
<tr><td> HR </td><td> 03 </td><td> Wheelchair - foldable </td><td> Wheelchair in which the traveller transfers to a seat </td><td>  </td><td> 1. Traveller must have a seat.                                                    2. Wheelchair can be folded up. Valid as luggage. </td><td> 1. Passenger accessible seat available                                                       2. Luggage space large enough for folded wheelchairs. </td><td>  </td><td> </td></tr>
<tr><td> HR </td><td> 04 </td><td> Wheelchair - cannot be secured responsibly </td><td> Wheelchair in which the traveller transfers to a  seat </td><td>  "irresponsibly lockable" and often not foldable.   </td><td> 1. Traveller must have a seat.                                                    2. Wheelchair must be carried in its entirety. Applies as luggage  </td><td> 1. Passenger accessible seat available                                                       2. Luggage space large enough for non-foldable wheelchairs. </td><td>  </td><td> </td></tr>
</table>



This is translated to a json structure with these properties:

| field | required | description |
| --- | --- | --- | 
| category | * | references to the first column of the specification<be>enum: [ HR, AV, HV, AB, AER, K, ZR, RR ] |
| number | * | references to the second column of the specification, length = 2 |
| type | | conditionally extra information, referencing to the 3rd column |
| memo | | extra field for detailed information, not standardized |
| variable-number | | in some requirements there is references to '[variable number]' e.g. of meters (like ZR06) |
| applicable-days | | days of the week that are applicable, list of enum: [MO, TU, WE, TH, FR, SA, SU] |
  
It results in JSON like this:
```
    "abilities": [
          {
            "category": "HR",
            "number": "01",
            "applicable-days": [
              "MO", "TU", "WE", "TH", "FR"
            ]
          }
        ]
```