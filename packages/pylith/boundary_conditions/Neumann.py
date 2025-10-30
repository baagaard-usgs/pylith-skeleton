import journal
import pylith

from .BoundaryCondition import BoundaryConditionBase


class Neumann(
    BoundaryConditionBase,
    family="pylith.boundary_conditions.neumann",
):
    """Neumann boundary condition.

        This boundary condition applies a Neumann boundary condition for a single solution subfield on a boundary.
        To apply Neumann boundary conditions for multiple solution subfields on a boundary, use multiple Neumann boundary conditions.

        :::{important}
        The components are specified in the local normal-tangential coordinate system for the boundary. Ambiguities in specifying the shear (tangential) tracti
    ons in 3D problems are resolved using the `ref_dir_1` and `ref_dir_2` properties.
        The first tangential direction is $\\vec{z} \\times \\vec{r}_1$ unless these are colinear, then $\\vec{r}_2$ (`ref_dir_2`) is used.
        The second tangential direction is $\\vec{n} \\times \\vec{t}_1$.
        :::

        :::{seealso}
        See [`AuxSubfieldsTimeDependent` Component](AuxSubfieldsTimeDependent.md) for the functional form of the time depenence.
        :::
    """

    scale_name = pylith.properties.str(
        default="stress",
        validator=pylith.properties.choice(["displacement", "stress"]),
    )
    scale_name.doc = "Type of scale for nondimensionalizing Neumann boundary condition ('stress' for elasticity)."

    use_initial = pylith.properties.bool(default=True)
    use_initial.meta["tip"] = "Use initial term in time-dependent expression."

    use_rate = pylith.properties.bool(default=False)
    use_rate.meta["tip"] = "Use rate term in time-dependent expression."

    use_time_history = pylith.properties.bool(default=False)
    use_time_history.meta["tip"] = "Use time history term in time-dependent expression."

    # time_history = db_time_history()
    # time_history.doc = "Time history with normalized amplitude."

    ref_dir_1 = pylith.properties.array(default=[0.0, 0.0, 1.0], validator=validateDir)
    ref_dir_1.doc = "First choice for reference direction to discriminate among tangential directions in 3D."

    ref_dir_2 = pylith.properties.array(default=[0.0, 1.0, 0.0], validator=validateDir)
    ref_dir_2.doc = "Second choice for reference direction to discriminate among tangential directions in 3D."

    def __init__(self):
        super().__init__(self)

        channel = journal.debug(":TODO:")
        channel.log("Implement Neumann time_history attribute. Requires spatialdata.")
        channel.log("Implement Neumann.__init__(). Pass parameters to C++.")
