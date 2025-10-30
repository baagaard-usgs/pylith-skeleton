import pylith
import journal


class Run(pylith.shells.command, family="pyre.cli.run"):
    """Run the application."""

    @pylith.export(tip="generate completions candidates from a partial command line")
    def main(self, plexus, argv, **kwds):
        # :KLUDGE: set default journal parameters
        journal.decor(1)
        journal.detail(1)

        plexus.run_cxx()
        return 0
