# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Quasistatic Example

    What goes here:
    * Text description of the problem
    * Diagram of the problem, identifying materials, boundary conditions, etc

    Normally, an example goes through the following steps.
    1. Create the finite-element mesh.
    2. Generate the spatial database files with values.
    3. Setup the simulation parameter file.
    4. Run the simulation.
    5. Visualize the results.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup top-level application

    1. Create application
    2. Set simulation metadata
    3. Set simulation defaults
    """)
    return


@app.cell
def _():
    # Import the application
    import pylith

    # Create the application
    app = pylith.shells.pylith(name="pylith_app")

    # Set simulation metadata
    app.metadata.authors = ["Brad Aagaard"]
    app.metadata.description = "Quasi-static simulation of axial compression of an elastic block using Dirichlet boundary conditions."

    # Set simulation defaults
    app.defaults.output_name = "elasticity-axial-extension"
    return app, pylith


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup boundary value problem

    1. Set mesh initializers
    2. Use default scales for nondimensionalization
    3. Use default governing equation (elasticity)
    """)
    return


@app.cell
def _(app):
    mesh_initializer = app.problem.mesh_initializer
    mesh_initializer.read_mesh.uri = "mesh_quad.msh"
    mesh_initializer.refine_mesh.levels = 1
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup governing equation

    1. Set PETSc options
    2. Set boundary conditions
    3. Set materials
    """)
    return


@app.cell
def _(app, pylith):
    governing_eqn = app.problem.governing_eqn

    # Set PETSc options
    petsc_options = governing_eqn.solver.petsc_options

    # :TODO: solver_options is not getting resolved to the group in pylith_app.yaml
    solver_options = pylith.petsc.options.groups.group_list(name="solver_elasticity_nofault")
    petsc_options.solver = solver_options
    petsc_options.initial_guess.enabled = True
    petsc_options.tolerances.enabled = True
    petsc_options.adaptive_ts.enabled = True

    # Set boundary conditions
    from pylith.boundary_conditions import dirichlet, neumann
    bc_xneg = dirichlet(name="bc_xneg")
    bc_yneg = dirichlet(name="bc_yneg")
    bc_xpos = neumann(name="bc_xpos")
    governing_eqn.boundary_conditions = [bc_xneg, bc_yneg, bc_xpos]

    # Set materials
    from pylith.governing_eqns.elasticity_eqn.bulk_rheologies import isotropic_linear
    crust = isotropic_linear(name="crust")
    governing_eqn.materials = [crust]
    return (solver_options,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Save configuration
    """)
    return


@app.cell
def _(app):
    app.pyre_persist(uri="qs_nb.yaml")
    return


@app.cell
def _(solver_options):
    print("\n".join(solver_options.pyre_showConfiguration()))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ```yaml
    pylith_app.problem.governing_eqn:
        solver: pylith.solvers.petsc
        materials:
            - pylith.governing_eqns.elasticity_eqn.bulk_rheologies.isotropic_linear#crust
        boundary_conditions:
            - pylith.boundary_conditions.dirichlet#bc_xneg
            - pylith.boundary_conditions.dirichlet#bc_yneg
            - pylith.boundary_conditions.neumann#bc_xpos
    ```
    """)
    return


if __name__ == "__main__":
    app.run()


# End of file
