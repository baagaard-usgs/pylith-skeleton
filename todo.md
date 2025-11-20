# To-do

1. Clean up solver options
   1. Create real components for simulation defaults and solver options.
   2. Create singletons for sets of options
   3. Create mock up for using solver options for a governing equation based on presence of fault and other parameters
2. Move protocols to a separate directory.
3. Test using MPI
4. Move fields "database" to C++ (used in MMS tests) [name, scale, vector_field_type, component_names]

- governing_eqns
  - IncompressibleElasticity
  - Poroelasticity
- materials
  - IncompressibleElasticity
  - Poroelasticity
- utils/VersionInfo.py
- dependencies
  - VersionInfo.py
