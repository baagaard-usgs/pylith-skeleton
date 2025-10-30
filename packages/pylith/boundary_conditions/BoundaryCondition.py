import pylith


class BoundaryCondition(pylith.protocol, family="pylith.boundary_conditions"):
    """Protocol declarator for boundary conditions."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {BoundaryCondition} implementation"""
        from .Dirichlet import Dirichlet

        return Dirichlet


class BoundaryConditionBase(pylith.component, implements=BoundaryCondition):
    """Base class for boundary conditions."""

    field = pylith.properties.str(default="displacement")
    field.doc = "Solution subfield associated with boundary condition."

    label_name = pylith.properties.str(validator=validateLabel)
    label_name.meta["tip"] = "Name of label identifying boundary ()name of physical group in Gmsh files."

    label_value = pylith.properties.int(default=1)
    label_value.meta["tip"] = "Value of label identifying boundary (tag of physical group in Gmsh files)."
