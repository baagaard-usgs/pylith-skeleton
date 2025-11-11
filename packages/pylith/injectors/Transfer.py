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
