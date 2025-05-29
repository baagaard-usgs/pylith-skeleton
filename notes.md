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

Configuration is handled before constructor is called.

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

florcor --shell=script

wihout commans.

flocore list (tab)

flocor config version

command line arguments as menu

for properties --dry

qed 

Plexus (application with menu driven)! [multiplexer] forwards command "panels" (2 levels)

* How to use journal within components? (No self.info, etc)

Components with journal. Build and attach journals in constructor. cls or instance.
Could create PyLith base component that turns on journal.

tests/journal.api
debug_example.py - base case
DEVICES
attach metadata to report; can control how much meadata

journal.lib (C++)
journal.pkg (python)

* Can protocols have Pyre properties and facilities or do I define a separate base class for facilities used by multiple components implementing the protocol?

* Example of using validator?

tests/pyre.pkg/coompoents/compnent_instance_validation.py component_class_validation.py.
Can use tuple of validators.

class property [all raw instances not configured can have new default]


* How to set default component for facility to None? Do I just not implement pyre_default in the protocol?

Default pyre_default class method returns None.



* How to reference a component in list of components in a .cfg file? [ pylith.problems.timedependent # pylith.problems#problem ]

* Why not use h5py?

* No nemesis? How are MPI jobs started? What is the difference between non-MPI and MPI applications?

mpi launcher is a shell. world.py

./world.py --shell=mpi.mpirun [how to activate MPI]

launxher.py ; --tasks [number of MPI tasks per host]
mpirun.py

* Possible to submit jobs on remote machines?

slurm.py [queue system]

REMOTE JOB SUBMISSION - still on TODO list

Can use ssh tunnel to frontend and submit. Would be nice to revive.
DOABLE

BEYOND what ssh supports, probably trigger security.

web app - use ssh tunnel to access port locally. Ask sysadmin if access is acceptable.

## Discuss context for using Pyre in Jupyter notebooks

* Building simulation parameter files from the top down with explanation
* Interactive help (seeing defaults, validating current settings)
* Writing parameter files

Underneath notebook is instance of Pyhton whose state accumulates side effects of cells.
Execute cells out of order. Have to restart kernel to get state. Anything that doesn't clean up properly will cause problems. New Pyre - can reconfigure component.

generator not a string for help -
can simplify  - could make PyLithApp - present so render however you want.

What is left behind by configuration, need something . PYRE TODO

## Discuss example of creating a GUI to construct simulation parameter files

Pyre app that can run web server as a client. (web not script shell)
Wiring together computation out of Pyre components. inputs and outputs from protocols.  Large collection of components within application or collection of components. Application as a workflow.

GUI - for setting paraemeters, etc. Could be done but not implemented.

Offering guidance of what possible information - more work.
Telling them what the options are is a bit more work but potentially doable. [hours]


TODO - draw diagram/sketch of GUI interface.
bootstrap pyre application.

templates/react sample pyre app Python layer and GUI.
flexi..yaml


smith --config=pylith.yaml
go to templates directory and make subdirectory.

## Go over installing Pyre 1.x using mm.

oyre/etc/docker
imposh-gcc

mm - pyre application
config.mm (where external dependencies live)
wher einstalled @PREFIX@

bldroot

make = make

pybind11


Dockerfile

Put mm file in correct place and config.mm will get me mm.
mpish-gcc

slack - INvite michael to pylith-dev workspace.

clone mm once.






