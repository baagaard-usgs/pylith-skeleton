import pylith


class About(pylith.shells.command, family="pyre.cli.about"):
    """Display information about this application."""

    @pylith.export(tip="Print the version number.")
    def version(self, plexus, **kwds):
        """Print the version."""
        info = pylith.journal.info_factory.about()
        info.log(pylith.meta.header)

    @pylith.export(tip="Print the license and terms of use.")
    def license(self, plexus, **kwds):
        """Print the license and terms of use."""
        info = pylith.journal.info_factory.about()
        info.log(pylith.meta.license)

    @pylith.export(tip="Print how to cite PyLith.")
    def how_to_cite(self, plexus, **kwds):
        """Print how to cite PyLith."""
        info = pylith.journal.info_factory.about()
        info.log(":TODO: how to cite")
