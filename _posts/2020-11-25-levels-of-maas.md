---
title: TOMP-API & Levels of MaaS 
categories:
- General
feature_image: "https://picsum.photos/2560/600?image=872"
---

The TOMP-API is a standard in MaaS ecosystems, but how does it relate to the ecosystem? In this article we try to find this out.  
The TOMP-API consists out of multiple modules, and some of them are directly related to a level in the “4 levels of MaaS” model as proposed by [Steven Sarasini](https://www.researchgate.net/figure/Proposed-topology-of-MaaS-including-Levels-0-4-left-and-examples-right_fig2_320107637). We address each level of the model and look to the related modules, or even roadmap items of the TOMP-API.

![4 Levels Of MaaS](/assets/4levelsOfMaaS-300x260.png)

1)     Integration of information: the complete “Operator Information” module is directly related here, except for the ‘meta’ endpoint (that is added for interoperability reasons). The multimodal travel planners in the ecosystem can use this information  
2)     Most of the modules, like planning, booking and payment are in this layer. This is where the core of the TOMP-API resides.  
3)     The integration at level 3 is supported by the ‘meta’ endpoint, where discovery services can look at, to find each other. But also the digital contracts (roadmap item) must be facilitated by the TOMP-API.  
4)     The last level is really at the top of the services and is already served by the TOMP-API by communicating data about end users, their abilities and the open setup to integrate with other ecosystem components, like ‘personal data stores’. The difference between level 3 and 4 is more about the usage of the API (the content of the messages) and not directly related to technical endpoints.
