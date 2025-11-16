# To-do

1. Test using MPI
2. Create subfields using type() DONE
3. Refactor petsc.options to use type() DONE
4. Create components to hold subfields (solution, auxiliary field, derived field)
   1. SubfieldBasic
   2. Density (name=density, scale=density, vector_field_type=scalar)
5. Setup nontrivial test case

- governing_eqns
  - IncompressibleElasticity
  - Poroelasticity
- materials
  - IncompressibleElasticity
  - Poroelasticity
- utils/VersionInfo.py
- dependencies
  - VersionInfo.py
