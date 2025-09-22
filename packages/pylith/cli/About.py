import pyre

import pylith


class About(pylith.shells.command, family="pyre.cli.about"):
    """Display information about this application."""

    @pyre.export(tip="Print the version number.")
    def version(self, plexus, **kwds):
        """Print the version."""
        major, minor, micro = pylith.version()
        plexus.info.log(f"Version {major}.{minor}.{micro}")

    @pyre.export(tip="Print the authors.")
    def authors(self, plexus, **kwds):
        """Print the authors."""
        plexus.info.log(pylith.meta.authors)

    @pyre.export(tip="Print the copyright.")
    def copyright(self, plexus, **kwds):
        """Print the copyright."""
        plexus.info.log(pylith.meta.copyright)

    @pyre.export(tip="Print the license and terms of use.")
    def license(self, plexus, **kwds):
        """Print the license and terms of use."""
        plexus.info.log(pylith.meta.license)

    @pyre.export(tip="Print the acknowledgments.")
    def credits(self, plexus, **kwds):
        """Print the acknowledgments."""
        plexus.info.log(pylith.meta.header)

    @pyre.export(tip="Print how to cite PyLith.")
    def how_to_cite(self, plexus, **kwds):
        """Print how to cite PyLith."""
        raise NotImplementedError(":TODO:")
