import journal
import pyre

import pylith
from pylith.apps import pylith_app


class Run(pylith.shells.command, family="pyre.cli.run"):
    """Run the application."""

    @pyre.export(tip="generate completions candidates from a partial command line")
    def main(self, plexus, argv, **kwds):
        # set default journal parameters
        journal.decor(1)
        journal.detail(1)

        app = pylith_app(name="pylith.app")
        status = app.run()
        return status
