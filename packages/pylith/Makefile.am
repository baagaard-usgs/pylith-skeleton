# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information. 
# =================================================================================================


if ENABLE_CUBIT
make-manifest:
else
make-manifest:
	echo "exclude meshio/MeshIOCubit.py" > $@
endif

install-exec-local: make-manifest
	$(PYTHON) -m pip install $(top_srcdir)

EXTRA_DIST = \
	__init__.py \
	apps/__init__.py \
	apps/PyLithApp.py \
	boundary_conditions/__init__.py \
	boundary_conditions/BoundaryConditionBase.py \
	boundary_conditions/Dirichlet.py \
	boundary_conditions/Neumann.py \
	cli/__init__.py \
	cli/About.py \
	cli/Config.py \
	cli/Debug.py \
	cli/Help.py \
	cli/Info.py \
	cli/Run.py \
	data_writers/__init__.py \
	data_writers/DataWriterBase.py \
	data_writers/DataWriterHDF5.py \
	data_writers/DataWriterVTK.py \
	defaults/__init__.py \
	defaults/SimulationDefaults.py \
	exceptions.py \
	fields/__init__.py \
	fields/discretizations/__init__.py \
	fields/discretizations/DiscretizationPetsc.py \
	fields/FieldBasic.py \
	fields/FieldOptional.py \
	fields/subfields/__init__.py \
	fields/subfields/SubfieldBasic.py \
	fields/subfields/SubfieldOptional.py \
	governing_eqns/__init__.py \
	governing_eqns/elasticity_eqn/__init__.py \
	governing_eqns/elasticity_eqn/bulk_rheologies/__init__.py \
	governing_eqns/elasticity_eqn/bulk_rheologies/ElasticityRheology.py \
	governing_eqns/elasticity_eqn/bulk_rheologies/IsotropicLinear.py \
	governing_eqns/elasticity_eqn/ElasticityEqn.py \
	governing_eqns/elasticity_eqn/solution_subfields/__init__.py \
	governing_eqns/elasticity_eqn/solution_subfields/SubfieldsFault.py \
	governing_eqns/elasticity_eqn/solution_subfields/SubfieldsNoFault.py \
	governing_eqns/GoverningEqnBase.py \
	initial_conditions/__init__.py \
	initial_conditions/InitialConditionBase.py \
	initial_conditions/InitialConditionDomain.py \
	initial_conditions/InitialConditionPatch.py \
	injectors/Transfer.py \
	interior_interfaces/__init__.py \
	interior_interfaces/FaultCohesive.py \
	interior_interfaces/FaultCohesiveImpulses.py \
	interior_interfaces/FaultCohesiveKinematic.py \
	interior_interfaces/source_time_fns/__init__.py \
	interior_interfaces/source_time_fns/Brune.py \
	interior_interfaces/source_time_fns/ConstantRate.py \
	interior_interfaces/source_time_fns/LuiCosine.py \
	interior_interfaces/source_time_fns/Ramp.py \
	interior_interfaces/source_time_fns/SourceTimeFnBase.py \
	interior_interfaces/source_time_fns/Step.py \
	interior_interfaces/source_time_fns/TimeHistory.py \
	journal/__init__.py \
	journal/DebugFactory.py \
	journal/ErrorFactory.py \
	journal/FirewallFactory.py \
	journal/InfoFactory.py \
	journal/WarningFactory.py \
	mesh_initializers/__init__.py \
	mesh_initializers/distributors/__init__.py \
	mesh_initializers/distributors/DistributorPetsc.py \
	mesh_initializers/MeshInitializer.py \
	mesh_initializers/phases/__init__.py \
	mesh_initializers/phases/MeshDistributor.py \
	mesh_initializers/phases/MeshInsertInterfaces.py \
	mesh_initializers/phases/MeshReader.py \
	mesh_initializers/phases/MeshRefiner.py \
	mesh_initializers/phases/MeshReordering.py \
	mesh_initializers/phases/MeshWriter.py \
	mesh_io/__init__.py \
	mesh_io/MeshIOAscii.py \
	mesh_io/MeshIOCubit.py \
	mesh_io/MeshIOPetsc.py \
	meshing/__init__.py \
	meshing/refiners/__init__.py \
	meshing/refiners/RefineUniform.py \
	meta.py \
	metadata/__init__.py \
	metadata/SimulationMetadata.py \
	monitors/__init__.py \
	monitors/ProgressMonitorBase.py \
	monitors/ProgressMonitorStep.py \
	monitors/ProgressMonitorTime.py \
	observers/__init__.py \
	observers/ObserverInjector.py \
	observers/output_triggers/__init__.py \
	observers/output_triggers/OutputTriggerStep.py \
	observers/output_triggers/OutputTriggerTime.py \
	observers/OutputObserver.py \
	observers/OutputPhysics.py \
	observers/OutputSolnBoundary.py \
	observers/OutputSolnDomain.py \
	observers/OutputSolnPoints.py \
	petsc/__init__.py \
	petsc/options/__init__.py \
	petsc/options/groups/__init__.py \
	petsc/options/groups/GroupList.py \
	petsc/options/ManagerBase.py \
	petsc/options/SimulationOptions.py \
	petsc/options/SolverOptions.py \
	problems/__init__.py \
	problems/GreensFns.py \
	problems/ProblemBase.py \
	problems/TimeDependent.py \
	protocols/__init__.py \
	protocols/ApplicationDefaults.py \
	protocols/ApplicationMetadata.py \
	protocols/BoundaryCondition.py \
	protocols/DataWriter.py \
	protocols/Field.py \
	protocols/fields/__init__.py \
	protocols/fields/Discretization.py \
	protocols/fields/Subfield.py \
	protocols/governing_eqns/__init__.py \
	protocols/governing_eqns/elasticity/__init__.py \
	protocols/governing_eqns/elasticity/BulkRheology.py \
	protocols/governing_eqns/elasticity/SolutionSubfields.py \
	protocols/GoverningEqn.py \
	protocols/InitialCondition.py \
	protocols/interior_interfaces/__init__.py \
	protocols/interior_interfaces/SourceTimeFn.py \
	protocols/InteriorInterface.py \
	protocols/mesh_initializers/__init__.py \
	protocols/mesh_initializers/Distributor.py \
	protocols/mesh_initializers/InitializePhase.py \
	protocols/meshing/__init__.py \
	protocols/meshing/Refiner.py \
	protocols/MeshInitializer.py \
	protocols/MeshIO.py \
	protocols/Observer.py \
	protocols/observers/__init__.py \
	protocols/observers/OutputTrigger.py \
	protocols/petsc/__init__.py \
	protocols/petsc/options/__init__.py \
	protocols/petsc/options/Group.py \
	protocols/petsc/OptionsManager.py \
	protocols/Problem.py \
	protocols/ProgressMonitor.py \
	protocols/Scales.py \
	protocols/Solver.py \
	scales/__init__.py \
	scales/DynamicElasticity.py \
	scales/ElasticityScales.py \
	scales/QuasistaticElasticity.py \
	scales/QuasistaticPoroelasticity.py \
	scales/ScalesBase.py \
	shells/__init__.py \
	shells/Action.py \
	shells/Command.py \
	shells/Plexus.py \
	solvers/__init__.py \
	solvers/SolverPetsc.py \
	utils/__init__.py \
	utils/constraints.py
