import pyre
import journal


class Component(pyre.component):
    """Abstract base class for PyLith components."""

    info = None
    debug = None

    def __init__(self, name=None, **kwds):
        super().__init__(name=name, **kwds)

        self.info = journal.info(self.pyre_name)
        self.debug = journal.debug(self.pyre_name)

    def welcome(self):
        self.info.log("Hello from {!r}".format(self.pyre_name))
        traits = self.pyre_configurables()
        for trait in traits:
            if isinstance(trait, Component):
                trait.welcome()
