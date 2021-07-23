# Open-Source DT Implementations

With this exemplar, we provide models that can be used by two open-source implementations of DT infrastructure. A description of setting up the required infrastructure to run the DTs for these models this is part of future work.

## Model-Integrated Runtime Monitoring Infrastructure
In [1], a runtime infrastructure to colelct data from a Cyber-Physical System is described. In the folder [monitoring](./monitoring), we provide an implementation of the proposed Meta-Model that can be used to automatically set up this infrastructure using the Eclipse Modeling Framework.
An example model describing required model elements for our air quality use case is provided in the folder [airquality](./airquality).

[1] Vierhauser, Michael, et al. "Towards a Model-Integrated Runtime Monitoring Infrastructure for Cyber-Physical Systems." 2021 IEEE/ACM 43rd International Conference on Software Engineering: New Ideas and Emerging Results (ICSE-NIER). IEEE, 2021.


## Eclipse Vorto
[Eclipse Vorto](https://www.eclipse.org/vorto) is a modeling tool to create Digital Twins that can be used by both [Eclipse Hono](https://www.eclipse.org/hono/) and [Eclipse Ditto](https://www.eclipse.org/ditto/index.html) to implement a DT Infrastructure (as e.g. described [here}(https://blog.bosch-si.com/developer/harmonizing-specific-device-payloads-using-eclipse-vorto/)). As part of this exemplar, we implemented publicly available DT models required to set up our air quality use case using the Eclipse Vorto Repository. However, as this repository is currently offline due to technical issues on the side of Eclipse, we are not able to provide a link to these models.
