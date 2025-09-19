import pyre


class Material(pyre.protocol, family="pylith.materials"):
    """Protocol declarator for materials."""

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Material} implementation"""
        from .Elasticity import Elasticity

        return Elasticity

    @pyre.provides
    def initialize(self):
        """Initialize material."""

    @pyre.provides
    def setState(self, t):
        """Set material state."""

    @pyre.provides
    def computeState(self, t):
        """Compute material state."""

    @pyre.provides
    def finalState(self, t):
        """Set material end state."""


class MaterialBase(pyre.component):
    # from pylith.observers import observer, observer_solution

    # observers = pyre.properties.list(schema=observer(default=observer_solution))
    # observers.doc = "Observer of material state."

    @pyre.export
    def finalState(self, t):
        """Set material end state."""
        # self.observer.update(t)


# class Injector(pyre.component, family="pylith.injectors.material"):
#    """Inject value into material state."""
#
#    target = Material()
#    target.doc = "Material to inject value into."
#
#    value = pyre.properties.float(default=2.0)
#    value.doc = "Value to inject."
#
#    @pyre.export
#    def setState(self):
#        """Update state."""
#        self.target.setState(self.value)


# class Transfer(
#    pyre.component, family="pylith.transfer.material", implements=(Observer, Injector)
# ):
#    """Transfer state from one object to another."""
#
#    target = Material()
#    target.doc = "Material to inject value into."
#
#    def __init__(self, **kwds):
#        """Constructor."""
#        super().__init__(**kwds)
#        self.t = None
#
#    @pyre.export
#    def update(self, t):
#        """Update observer."""
#        self.t = t
#        self.setState()
#
#    @pyre.export
#    def setState(self):
#        """Update state."""
#        self.target.setState(self.t)
