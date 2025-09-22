import pyre

import pylith


class Config(pylith.shells.command, family="pylith.cli.config"):
    """
    Display configuration information about this package
    """

    @pyre.export(tip="Print the top-level installation directory.")
    def prefix(self, **kwds):
        """Print the top level installation directory"""
        print(f"{pylith.prefix}")
        return 0

    @pyre.export(tip="Print the directory with the executable scripts.")
    def path(self, **kwds):
        """Print the location of the executable scripts."""
        print(f"{pylith.prefix}/bin")
        return 0

    @pyre.export(tip="Print the directory with the Python packages.")
    def pythonpath(self, **kwds):
        """Print the directory with the Python packages"""
        print(f"{pylith.home.parent}")
        return 0

    @pyre.export(tip="Print the location of the PyLith headers")
    def include_path(self, **kwds):
        """Print the locations of the PyLith header files."""
        print(f"{pylith.prefix}/include")
        return 0

    @pyre.export(tip="Print the location of the PyLith libraries.")
    def library_path(self, **kwds):
        """Print the locations of the PyLith libraries."""
        print(f"{pylith.prefix}/lib")
        return 0
