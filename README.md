# An Exemplar for Model-Driven Digital Twin Development
<a href="https://cdl-mint.se.jku.at/" >
<img alt="Qries" align="Right" src="https://cdl-mint.se.jku.at/wp-content/uploads/2019/04/CDL-MINT.png"
width=120" height="120">
</a>

This repository provides all source code + documentation for setting up an air quality use case, together with the respective Digital Twins to collect air quality data and applications that make use of these DTs.
                       
## Use Case Description
As the air quality within a room is correlation with concentration levels of office workers or the spread of viruses, it is interesting for organizations of different kinds to manage this air quality within their buildings, to ensure safety and production of employees, customers, or students. Therefore, air quality can be measured using metrics such as CO2 concentration, humidity or temperature values. If these values exceed certain threshold values, this bad level of air quality might have a negative impact of people within a room. Identifying such threshold violations and deriving appropriate measures can be used to ensure a certain air quality within the rooms of a building.

## Contents of this Exemplar Repository
1. Implementation of Physical Twin: To set up the hardware required to implement the physical twin of the room, we provide a detailed description of used hardware, setup procedures, and automation scripts in [this folder](./physical_twin/hardware_setup). For testing purposes, we also provide a simulations scripts that mocks the hardware using random values for different air quality measures in [this folder](./physical_twin/simulated_hardware).
2. Implementation of Digital Twin: As an industry-scale implementation of Digital Twins and required infrastructure to run them, we provide documentation and code for setting up the DTs for the provided physical twins using existing PaaS-tools provided by Microsoft Azure in [this folder](./digital_twin/azure). We also provide two open-source alternatives for this Azure implementation in [this folder](./digital_twin/open-source).
3. Applications: As applications that make use of the implemented DT, we provide a [mobile app for visualization](./applications/visualisation), a [physical simulation model](./applications/physical_modelling), and a [prediction service](./applications/machine_learning). 
