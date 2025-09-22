import pyre
import journal

import pylith


# declaration
class Plexus(pyre.plexus, family="pylith.shells.plexus"):
    """The main action dispatcher."""

    from .Action import Action as pyre_action

    # journal control; useful until journal is once again configurable
    logfile = pyre.properties.path()
    logfile.default = None
    logfile.doc = "File that captures all journal output"

    def __init__(self, **kwds):
        super().__init__(**kwds)
        if self.logfile:
            # redirect all journal output to the file
            journal.logfile(name=str(self.logfile), mode="a")
