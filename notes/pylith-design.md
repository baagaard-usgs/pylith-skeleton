# PyLith Design

## Application

- Application defaults (name, output directory)
- PETSc options (general PETSc options)
- Metadata (author, description, keywords, etc)
- Problem

## PETSc options

- Collective I/O
- Testing (malloc_debug)
- Attach debugger

1. Want to enable/disable groups of options
2. Groups should be easily extensible by users and PyLith developers.
3. Loop over groups to assemble list of all options to pass to PetscInitialize(). 

### Options group

- enabled: Flag indicating whether group of options is enabled or disabled.
- list(tuple(str)): list of options

## Problem

- Mesh initializer (reading and preprocessing the mesh)
- Scales (for nondimensionalization)
- Governing equation

## Governing equation

- Solver (PetscSolver)
- Solution (solution field - container of subfields)
- Boundary conditions (can be a list of named objects)
- Initial conditions (can be a list of named objects)
- Interior interfaces (can be a list of named objects)
- Observers (can be a list of named objects)

1. User can customize the discretization of each solution subfield (Pyre properties).
2. The solution field spans all degrees of freedom of the domain.
3. The subfields of the solution field are set based on the governing equation used.
4. Subfield not be defined at all degrees of freedom, for example, the Lagrange multiplier field only exists for degrees of freedom on cohesive cells (interior interfaces).
5. Integration of terms in the finite-element weak form is done by Integrators (domain, boundary, interface). The physics is implemented via point-wise functions (integration of terms in weak form; projection of fields for output) associated with each material, boundary condition, and interface. Point-wise functions are passed the auxiliary field and the solution field evaluated at the (quadrature) point.
6. Can have an arbitrary number of boundary conditions, initial conditions, and interior interfaces.

### Elasticity governing equation

- Materials (default=materials.Elasticity)

### Incompressible elasticity governing equation

- Materials (default=materials.IncompressibleElasticity)

### Poroelasticity governing equation

- Materials (default=materials.Poroelasticity)

## Material

- Bulk rheology (linear elastic, Maxwell viscoelastic, Drucker-Prager elastoplasticity, etc)
- Material properties and state variables (auxiliary field with subfields)
- Derived subfield (subfields that can be derived from solution and auxiliary field)
- Observers (list of named objects)

1. A material is associated with a group of domain cells identified by label (name, value).
2. Can have multiple materials of the same type (different specifications of material properties).
3. Users can customize discretization of subfields of auxiliary field and derived field.
4. Auxiliary field is defined only over the cells associated with the material (subdomain); for boundary conditions, the auxiliary field is defined only over the boundary and likewise for interfaces.
5. Some subfields of the auxiliary field are optional (for example, body forces, gravitational acceleration).
6. Derived fields are optional. Want to be able to enable/disable each subfield.

## Field - container of subfields

## Subfield

- name
- alias (for output)
- scale (used in nondimensionalization)
- vector field type
- discretization (basis order, basis, etc)

1. PETSc Section holds mapping from points (vertices, edges, faces, cells) to degrees of freedom for each subfield.
2. PETSc Vec (array) holds values at degrees of freedom.

## Solver

### PETSc solver

Want to enable/disable groups of options

- Solver options (defaults based on governing equation; preconditioner, etc)
- Tolerances (SNES, KSP)
- Initial guess
- Adaptive time-stepping
- Monitoring (TS, SNES, KSP)
