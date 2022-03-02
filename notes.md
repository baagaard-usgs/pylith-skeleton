# Topics

2022-03-02 meeting with Michael Aivazis

## PyLith skeleton

- PyLithApp
  - SimulationMetadata
  - Problem
     - TimeDependent
  - BoundaryConditions
     - DirichletBC
     - NeumannBC
  - Materials
     - Elasticity
     - IncompressibleElasticity
  - Observer, Injector
    - ObserverSolution
    - Transfer

## Get a quick summary of primary features of Pyre 1.x

- merlin
- opal
- pyre
 - algebraic
 - calc
 - constraints
 - db
 - descriptors
 - flow
 - framework
 - http
 - ipc
 - nexus
 - records
 - smith
 - tracking
 - traits

## Questions:

* How to get help using the command line? How to show component locator in help?

* How to use journal within components? (No self.info, etc)

* Can propocols have Pyre properties and facilities or do I define a separate base class for facilities used by multiple components implementing the protocol?

* Example of using validator?

* How to set default component for facility to None? Do I just not implement pyre_default in the protocol?

* How to reference a component in list of components in a .cfg file? [ pylith.problems.timedependent # pylith.problems#problem ]

* Why not use h5py?

* No nemesis? How are MPI jobs started? What is the difference between non-MPI and MPI applications?

* Possible to submit jobs on remote machines?

## Discuss context for using Pyre in Jupyter notebooks

* Building simulation parameter files from the top down with explanation
* Interactive help (seeing defaults, validating current settings)
* Writing parameter files

## Discuss example of creating a GUI to construct simulation parameter files

## Go over installing Pyre 1.x using mm.


