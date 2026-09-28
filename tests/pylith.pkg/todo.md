# To-do

## Configuration tests

### Done

- application_defaults
- boundary_conditions
- data_writers
- fields
- governing_eqns
- initial_conditions
- journal
- mesh_io
- meshing
- mesh_initializers
- metadata
- monitors
- petsc
- observers
- scales
- solvers

### Missing

- fields [not used; subfields only (tested)]

- interior_interfaces
- interior_interfaces/source_time_fns

- apps
- utils

### Issues

Can't use full name specification.

```yaml
pylith.fields.subfields.basic#bulk_modulus
pylith.petsc.options.simulation_options#options:
pylith.governing_eqns.elasticity_eqn.bulk_rheologies.isotropic_linear#iso_test:
pylith.governing_eqns.elasticity_eqn.solution_subfields.fault#solution_field:
```

### Check/Fix

- problems

## full-scale

- about
- config
- debug
- help
- info
- run