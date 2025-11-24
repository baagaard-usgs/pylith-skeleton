import pylith


class Run(pylith.shells.command, family="pyre.cli.run"):
    """Run the application."""

    @pylith.export(tip="generate completions candidates from a partial command line")
    def main(self, plexus, argv, **kwds):
        try:
            plexus.run_cxx()
        except pylith.exceptions.PyLithError:
            import pdb

            pdb.set_trace()
        return 0
