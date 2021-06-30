Physical Modeling for the AirQuality Sensor



1 Documentation of the Physical Modelling

1.0.1 Translating the Geometrical Data into a Computational Model

Computational modelling is a very good time and money sparing tool which is a method for non-

destructive investigation. Most of all the analysed system can be put into complex scenarios which

wouldn’t be possible in real life.

1





1.1 Existing Air Quality Physical Models of Rooms

2





1.2 Applications of the Digital Room Model

There are many biomechatronic applications where the virtual model would be very useful. One

such application would deﬁnitely be in simulating the ﬂuid ﬂow in the Room and exchange between

people and analysing the FSI (velocity changes) in order to understand the air quality of the room.

Another application would be placing raspberries in diﬀerent areas of the room and analysing

the geometrical changes to the CO2 particles. This could be in context of FSI when placing a

raspberry or in another context.

3





2 Modelling the Virtual Room with the Air Particles

Out of the several layers of the room (epicardium, myocardium and endocardium), the endocardium

of the LV was considered. [ﬁg.??]This is because the endocardium is the innermost layer having

contact with the ﬂuid ﬂow (blood).

The top structure of the LV was modelled in order to have an in- and outlet ﬂow of ﬂuid to and

from the LV. For modelling the blood, SPH was considered on Abaqus. Python Scripting was used

to read in the input data for the geometry of the time states.

On Abaqus the simulation was created as a Dynamic Explicit Step with the units: mm,t and s.

All of the details on how each geometry was created on the FE program of Abaqus will be discussed

in the following sections.

4





2.1 Modelling the Shape of the Room

The walls of the room (the nodes) are deformed by boundary conditions. [ﬁg.??] As the boundary

conditions were considered, the material was not important and therefore also not included in the

settings of Abaqus.

The element shapes on consisted of 1595 rows and 3 columns. The rows represented the number

of elements and and the columns the respective nodes belonging to each element. [?]

These raw data were then translated into an input ﬁle for Abaqus. This was done by writing a

python script on jupyter.

2.2 Model Driven Engineering Techniques

Figure 2.1: Comparing Abaqus with the IoT

5





2.3 Modelling the CO2 source(s) in the room

The geometries of the source(s) were taken from the paper of Caballero. [?] The dynamic behaviour

was modelled such that they were ﬁxed in their positions (the setting on Abaqus was "ENCASTRE").

Figure 2.2: The CO2 source

Since the SPH formulation in Abaqus lacks periodic boundary conditions, the tubes were ex-

tended long enough to accommodate the in- outﬂow of particles for 2 full cycles. The tubular

structure had a diameter of 36.8mm and length started ﬁrst with 20mm which was then extended

depending on the need for the ﬂuid ﬂow. [ﬁg.\[2.1\]](#br5)[ ](#br5)In the end the For better modelling of the CO2

sources, the hollow shapes could be extended.

6





2.4 Modelling the Fluid Flow (Air Particle Properties-SPH particles)

The SPH modelling method is a meshless Lagrangian numerical technique that is modelled by an

equation of state on Abaqus(which is a research engineered data). It is a computational model to

model the ﬂuid for simulating ﬂuid ﬂow. Through such a method, problems involving large mesh

distortions can be solved with high accuracy.

SPH is usually chosen over the modelling needs in which traditional methods (FEM, FDM) fail

or are ineﬃcient. In extreme ﬂuid ﬂow where CFD (mesh or grid-based) cannot cope (free surface).

The novelty of SPH lies in the smooth interpolation and diﬀerentiation within an irregular grid of

moving macroscopic particles. Because nodal connectivity is not ﬁxed; severe element distortion is

avoided; hence the formulation allows for very high strain gradients.

The way SPH methods work is by dividing ﬂuid into discrete elements referred to as PC3D.

These SPH discrete elements (also considered as particles) have spatial distance known as smoothing

length.

The conservation of mass, linear, momentum and energy are exactly satisﬁed. SPH analysis

is an abaqus/explicit capability implemented for three-dimensional models. Initial and boundary

conditions can be speciﬁed as for any lagrangian model. Concentrated nodal loads can be applied

in the usual way, but the only distributed load type allowed is gravity. The only limitation is that

particle elements are not currently supported in Abaqus CAE.

7





2.4.1 Settings on Abaqus for Air Particles

The particle generator of air was used on Abaqus with the following incompressible characteristics

of air particles:

\- newtonian ﬂuid of density:

ρ = 1056kg/m3

(2.1)

(2.2)

B

\- dynamic viscosity:

µDyn = 0.0035Pa ∗ s

A general procedure for setting up SPH particles on Abaqus follows this order:

\1. Create a part for the SPH particles.

\2. Create an auxiliary continuum solid mesh with as much regularity as possible to reduce inac-

curacies.

\3. Create a node set that includes all the nodes of the auxiliary mesh.

\4. Create dummy mass elements at the nodes of the auxiliary mesh.

\5. Create the material.

\6. Instance the SPH part.

\7. Apply the initial and boundary conditions.

\8. Request ﬁeld and history output.

\9. Write input ﬁle.

\10. Modify the input ﬁle in a text editor:remove the auxiliary continuum solid mesh ﬁle.

\11. Change the mass elements to PC3D particle elements.

\12. Remove the dummy \*MASS option from the ﬁle and in its place use the \*SOLID SECTION

option to specify the properties of the particle elements.

\13. Deﬁne a node-based surface that includes all the SPH particles.

\14. Deﬁne contact interactions between the node-based particle surface and other surfaces in the

model.

In order to model the ﬂuid ﬂow the ﬁle was generated with SPH particles moving in and out

of the source. The nodes start from 2224 and go to 175069 nodes (in total 172845 nodes). The

total number of elements were 175068-3055=172013 elements. For the element set the solid section

keyword had to be implemented. (See [ﬁg.\[2.2\])](#br6)

8





Figure 2.3: Keywords needed for producing the input ﬁle of the SPH air particles

9





2.4.2 Dynamic Fluid Flow in and out of the LV on Abaqus

The dynamic movements of the virtual room gain importance when ﬂuid ﬂow is happening. In

other words air circulation wouldn’t be possible if there were no time states for a full cycle.

10





Therefore the master input ﬁle for Abaqus, the ﬁlling was written with the following scripting

[(ﬁg.\[2.3\]).](#br9)[ ](#br9)The end and start values [(ﬁg.\[2.4\])](#br11)[ ](#br11)were taken as displacement values in the Abaqus

[master](#br9)[ ](#br9)input ﬁle as a displacement for the [nodes](#br11)[ ](#br11)in the input ﬁle .

Figure 2.4: Master Scripting ﬁle on Abaqus for the inﬂow of air

And for the end state, the following script was written on the master ﬁle for Abaqus. [ﬁg.\[2.4\]](#br11)

Figure 2.5: Master Scripting ﬁle on Abaqus for the outﬂow of air

11





2.4.3 Limitations of the SPH Particles on Abaqus:

Unfortunately if the nodes are not placed in a regular cubic arrangement the initial mass is dis-

tributed inexactly. This happens particularly at the free surfaces. Additionally surface loads cannot

be speciﬁed on PC3D elements.

Another limitation is that mixing nodes with dissimilar materials cannot be modelled. However,

apart from these limitations, the using SPH particles was a suitable choice for the modelling of the

air circulation inside of the room.

12





2.5 The Complete Model of the Virtual Room

In order to complete the entire model of the virtual room, all of the input ﬁles were included in the

master input ﬁle (see ﬁgures [2.5](#br11)[ ](#br11)and [2.6.](#br13)[ ](#br13)The next subsections will discuss which complete model

of the virtual room had the [best](#br11)[ ](#br11)ﬁt.

Figure 2.6: Including the input ﬁles on Abaqus

13





Additionally the surface and surface sections for the elements were also deﬁned in the master

ﬁle. It was also important to deﬁne the amplitude values for the displacement values which were

then also scripted right below the surface and surface sections. [ﬁg.\[2.6\]](#br13)

Figure 2.7: Setting the surfaces of the elements and amplitudes for the time states end and start

14





2.5.1 Virtual Room with Short Sources

The initial model of the virtual room with the geometries taken from the Caballero paper resulted

in some stability issues and less control of the movements of the air particles on Abaqus which is the

reason the model was then modiﬁed into a virtual room model with longer sources (see following

subsection).

15





The ﬁg.[??] shows the odB ﬁle (output ﬁle) of the scripted input ﬁle by blending out the outer

layer and having a direct view on the particles.

16





Afterwards this output ﬁle was also analysed regarding the speed of the blood particles. From

ﬁg.[??] at the color coding table for velocities it is clearly visible that the blood particles gain in

velocity towards the buttom tip of the LV. It is also visible that when comparing the velocity of the

endocardium (movement of ED to ES and vice versa) to the speed of the movements of the blood

particles, the SPH particles are much faster.

However, in order to have a better perspective on the movement of the blood particles. The tubes

were elongated and analysed once again to have a more realistic control on the blood circulation

inside of the LV . Realistic in the sense that the inﬂow of the blood from the LA into the endocardium

also could have a smooth outﬂow towards the aorta. This will be discussed in the following.

17





2.5.2 The Diﬀerent Sources in Detail

For this thesis the leadless pacemaker of Medtronics was used (the Micra Model). ﬁg.[??]. The

geometric speciﬁcations of the pacemaker to model on Abaqus was taken from ﬁg.[??].

The reason of choice for a leadless pacemaker was regarded in terms of modelling purposes but

even as such there are also many advantages regarding the health of the patient. The beneﬁts for

modelling purposes are that the smaller the model, the easier it is to model on Abaqus. And also

the less prone the model is to mistakes. Therefore the leadless pacemaker of the micra model of

medtronics was chosen because of it being the world’s smallest pacemaker. [?]

18





So in order to build the part on Abaqus, a new part was created on Abaqus with the option

of not using parts and assemblies in the input ﬁles.(ﬁg.[??]) This step was important in order to

generate new nodes and elements for the pacemaker which would, however be renumbered starting

from the last node and element of the LV.

Figure 2.8: Building Part on Abaqus

In order to renumber the nodes of the pacemaker, the settings on [ﬁg.\[2.8\]](#br19)[ ](#br19)was chosen. This

setting could be reached via editing the mesh on Abaqus.

Figure 2.9: Renumbering nodes of the pacemaker to include in the master input ﬁle

Since it was not enough to only renumber the nodes but also necessary to renumber the elements,

the following renumbering settings on ﬁg.[??] had to be additionally applied.

19





Figure 2.10: Renumbering elements of the pacemaker to include in the master input ﬁle

Afterwards it was possible to mesh the source with quadrilateral R3D4 elements, as seen in

[ﬁg.\[2.10\].](#br20)

Figure 2.11: Model of Source

20





3 Conclusion

Overall building a FE model of a virtual LV on Abaqus is possible and easy to handle if the nodes,

elements and time states of the position of the nodes as displacements are given from accurate

measurements. As was the case in this thesis, where the data of the nodes and elements were taken

from the oﬃcial CAP website.

The interesting application came into play when analysing how the virtual LV model could be

used in a biomechatronics context. For this, ﬁrst the blood particles were included in the model

and then the FSI was analysed with and without the embedded pacemaker. It was clearly visible

through the simulation time and eﬀort that analysing the FSI of the LV without the embedded

pacemaker was much faster in results. A clear view on the color coding of the velocity of blood

showed that the SPH particles had higher velocities at the LA than at any other area of the LV.

This was also the case with the embedded pacemaker at the endocardium.

Analysing the FSI of the LV with the embedded pacemaker was a very important biomecha-

tronics context for clinical purposes, however also very challenging. This will be further discussed

in the following subsection.

21





3.1 Limitations and Suggested Improvements

Building the model gets challenging the moment one tries to go into more detail of how a LV should

look by including all of the other biological details such as the papillary muscles.

Therefore, instead of analysing the diﬀerent biological structures that could have been added to

the LV to test the validity and usefulness of the model. It was decided to keep the endocardium

layer of the LV and see what happens to the model with the embedded pacemaker. This proved to

be challenging in terms of modelling the ﬂuid ﬂow inside of the LV. In other words, it was more

challenging moving the blood particles in a resembling matter to the reality than modelling the

endocardium. The challenges included the missing computing power for faster simulations and due

to the complexity of real blood properties.

Adding a pacemaker in order to see how the FSI of the LV changes added another challenge

due to limited knowledge of how a pacemaker should be placed properly on the endocardium for

minimal invasion on the blood circulation.

All in all, building and simulating a LV on Abaqus as a FE model seems to be a good choice

when analysing the mechanical movements of a structure. This lies in the fact that Abaqus has its’

root in mechanical engineering. When trying to do a FSI, the limits of understanding of real blood

particles and modelling these as such on a FE model come into surface.

22





4 Outlook

A future outlook for a virtual room would be for augmented rooms

There is a wide future perspective in wearable technology, sensing and cloud computing. With

a good accurate model of a virtual LV diseases of a patient could be predicted.

23





References

[1] http://www.vhlab.umn.edu/atlas/, 2020.

24


