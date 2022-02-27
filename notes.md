PyLithApp
  SimulationMetadata
  Problem
    - TimeDependent
  BoundaryConditions
    - DirichletBC
    - NeumannBC
  Materials
    - Elasticity
    - IncompressibleElasticity

## Questions:

* How to get help using the command line? How to show component locator in help?
* How to use journal within components? (No self.info, etc)
* Can propocols have facilities or do I define a separate base class for facilities used by multiple components implementing the protocol?
* Example of using validator?
* How to set default component for facility to None?
* How to reference component in facility array in .cfg file? [ pylith.problems.timedependent # pylith.problems#problem ]
* Why not use h5py?
* Brief summary of packages
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
	* No nemesis? How are MPI jobs started? What is the difference between non-MPI and MPI applications?
	* Possible to submit jobs on remote machines?


## TODO


### Skeleton components for earthquake cycle

* PyLithApp
  * SimulationMetadata
  * Problems
  * TimeDependent
  * Material
    - Elasticity
    - Poroelasticity
  * BoundaryConditions
    - DirichletBC
    - NeumannBC
  * Observer (update)
  * Injector (setState)
  * Transfer (implements observer and injector)

### Jupyter notebook skeleton

Configure component hierarchy

