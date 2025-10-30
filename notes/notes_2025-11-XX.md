# Notes

## Configuration

1. I want to set defaults for the mesh initialization phases in `mesh_initializers.MeshInitializer` and allow them to be overwritten by the user. I have put the values in `serial_phases.yaml`. This is an application (not user) configuration file. How do I load it?

2. Similar to #1, but I want to add to a list of PETSc options based upon use of a component or a user flag.

    ```yaml
    pylith.app.petsc_options:
        testing: True
    ```

    ```python
    # pylith.petsc.options.OptionsManager
    if self.testing:
        pyre.loadConfiguration("petsc-testing.yaml")
    ```

    ```yaml
    # petsc-testing.yaml
    pylith.app.petsc_options:
      # Use different key (options-testing?) if we are appending manually to avoid overwriting?
      options:
        - malloc
        - malloc_debug
        - malloc_dump
    ```

3. What is the relationship between the family name for a component and the name in __init__? In udnerstand why it is nice that they match, but must they be the same?

    ```python
    # pylith/problems.__init__.py
    from pylith.problems.TimeDependent import TimeDependent as time_dependent

    # pylith/problems/TimeDependent.py
    class TimeDependent(pylith.protocol, implements=Problem, family="pylith.problems.time_dependent"):
    ```

## Pyre filesystem

1. We want to specify a default output directory and root for output files. What Pyre features might help with this?

## Code review

1. `shells/Plexus.py`
2. `cli/Run.py`
3. `mesh_initializers/MeshInitializer.py`
4. `mesh_initializers/phases/MeshRefiner.py`
