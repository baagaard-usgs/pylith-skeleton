# Notes

## Installation

1. How do I set `isysroot`?
2. C++ error

## Default configuration settings

1. `$src_topdir/etc/pylith/pylith.app.yaml` is not getting read. `pylith_plexus` is in `$src_topdir/bin`.

## Pyre configuration

1. How do I include multiple YAML files on the command line?

    Does not work (neither YAML file appears to be read)

    ```bash
    pylith_plexus --config=FILENAME1.yaml,FILENAME2.yaml
    ```

2. How do I get Pyre to report errors when it tries to instantiate an object and it fails? I don't seem to be getting any reports of configuration errors.

3. How do I programmatically create a component with values for properties? I want to set values so validation passes (for example, a `material` requires `label_name` to be provided by the user)

    ```python
    mat_elastic = pylith.materials.elasticity(label_name="material-id", label_value=2)
    ```

4. I want to create a dictionary of components that I can refer to in a nested sense. I think this is pyre.properties.dict() but I don't know how to use it.

    CIG Pyre (Leif Strand)

    ```cfg
    [ materials.elasticity ]
    auxiliary_fields = [density, shear_modulus, bulk_modulus]
    auxiliary_fields.density = pylith.fields.basic
    auxiliary_fields.shear_modulus = pylith.fields.basic
    auxiliary_fields.bulk_modulus = pylith.fields.basic    
    ```

    General defaults set via application provided configuration file

    ```yaml
    materials.elasticity: # Application defaults set via configuration settings
        auxiliary_fields: # Want this to be a dictionary
            - basic#density
            - basic#shear_modulus
            - basic#bulk_modulus
    ```

    Simulation-specific via configuration settings

    ```yaml
    materials:
        - elasticity#crust
        - elasticity#mantle

    crust:
        auxiliary_fields:
            density.discretization.basis_order: 0
            shear_modulus.discretization.basis_order: 0
            bulk_modulus.discretization.basis_order: 0
    
    mantle:
        auxiliary_fields:
            density.discretization.basis_order: 1
            shear_modulus.discretization.basis_order: 1
            bulk_modulus.discretization.basis_order: 1
    ```

5. Are nested components supposed to work in YAML files?

    Does not work:

    ```yaml
    pylith.materials.elasticity:
        auxiliary_subfields: # fields.field(default=fields.optional)
            required:
                - basic#density
            optional:
                - basic#body_force
                - basic#gravitational_acceleration
    ```

    Does work:

    ```yaml
    pylith.materials.elasticity:
        auxiliary_subfields: optional#elasticity_auxiliary_subfields

    pylith.fields.optional#elasticity_auxiliary_subfields:
        required:
            - basic#density
        optional:
            - basic#body_force
            - basic#gravitational_acceleration
    ```

6. It would really help if `pyre_showConfiguration(deep=True)` traversed into lists of objects.
