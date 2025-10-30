import journal
import pylith

from pyre.units.length import meter

from .BoundaryCondition import BoundaryConditionBase


class Dirichlet(BoundaryConditionBase, family="pylith.boundary_conditions.dirichlet"):
    """Dirichlet boundary condition."""

    constrained_dof = pylith.properties.array(converter=int)
    constrained_dof.doc = "Array of constrained degrees of freedom (0=1st DOF, 1=2nd DOF, etc)."

    use_initial = pylith.properties.bool(default=True)
    use_initial.meta["tip"] = "Use initial term in time-dependent expression."

    use_rate = pylith.properties.bool(default=False)
    use_rate.meta["tip"] = "Use rate term in time-dependent expression."

    use_time_history = pylith.properties.bool(default=False)
    use_time_history.meta["tip"] = "Use time history term in time-dependent expression."

    # time_history = db_time_history()
    # time_history.doc = "Time history with normalized amplitude."

    def __init__(self):
        super().__init__(self)

        channel = journal.debug(":TODO:")
        channel.log("Implement Dirichlet time_history attribute. Requires spatialdata.")
        channel.log("Implement Dirichlet.__init__(). Pass parameters to C++.")
