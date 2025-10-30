# Layout

## To-do

- Problem
  - governing_equation
- Petsc options
- GoverningEquation

## Python directory structure

- shells
  - `Plexus` (PyLith application)
- cli
  - `About`
  - `Config`
  - `Debug`
  - `Help`
  - `Info`
  - `Run`
- apps
  - `ConvertMeshApp`
  - `PyLithRunner`
  - `VizApp`
- problems
  - `Problem`
  - `GreensFns`
  - `TimeDependent`
- boundary_conditions
- initial_conditions
- faults
- materials
- observers
- scales
- mesh_io
- data_writers
- mesh_initializers
- viz
- shells
- monitors
- solution_fields
- meshing
- petsc
- utils

## C++ directory structure

- `apps`
  - `PyLithApp`
  - `ConvertMeshApp`
- `problems`
  - `Problem`
  - `GreensFns`
  - `TimeDependent`
- `equations`
  - `base` (physics)
  - `elasticity`
    - `materials`
    - `bulk_rheologies`
    - `solution`
    - `solver`
  - `incompressible_elasticity`
  - `poroelasticity`
- `boundary_conditions`
- `initial_conditions`
- `faults`
- `materials`
- `observers`
- `scales`
- `mesh_io`
- `data_writers`
- `mesh_initializers`
- `viz`
- `shells`
- `monitors`
- `solution_fields`
- `meshing`
- `petsc`
- `utils`

## Components

- Equations
  - GoverningEqn
    * solution
    * solver_settings
  - elasticity
    - Solution
    - SolverSettings
  - incompressible_elasticity
    - Solution
    - SolverSettings
  - poroelasticity
    - Solution
    - SolverSettings
  - base
    - Solution
    - SolverSettings

- constraints
  - ConstraintSimple
  - ConstraintSpatialDB
  - ConstraintCxxFn
- integrators
  - IntegrationManager
  - IntegrationData
  - Integrator
  - IntegratorDomain
  - IntegratorBoundary
  - IntegratorInterface

- Subfield
- Discretization
- Quadrature

- InitialCondition
- InitialConditionPatch
- InitialConditionDomain

- MeshIO
- MeshIOAscii
- MeshIOCubit
- MeshIOPetsc
