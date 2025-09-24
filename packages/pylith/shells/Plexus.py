import pyre
import journal

from pylith.metadata import metadata as app_metadata
from pylith.problems import problem
from pylith.problems import time_dependent


class Plexus(pyre.plexus, family="pylith.shells.plexus"):
    """The main action dispatcher."""

    from .Action import Action as pyre_action

    metadata = app_metadata()
    metadata.doc = "Application metadata"

    problems = pyre.properties.list(
        schema=problem(default=time_dependent),
        default=[time_dependent(name="problem")],
    )
    problems.doc = "Problems to solve."

    # journal control; useful until journal is once again configurable
    logfile = pyre.properties.path()
    logfile.default = None
    logfile.doc = "File that captures all journal output"

    def __init__(self, **kwds):
        super().__init__(**kwds)
        if self.logfile:
            # redirect all journal output to the file
            journal.logfile(name=str(self.logfile), mode="a")
