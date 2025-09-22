from pyre import executive

package = executive.registerPackage(name="pylith", file=__file__)
home, prefix, defaults = package.layout()


from . import shells
from . import meta
from . import cli


def version():
    """Return the version."""
    return meta.version


def copyright():
    """Return the copyright."""
    return print(meta.header)


def license():
    """Return the license."""
    return print(meta.license)


def credits():
    """Return the acknowledgments."""
    return print(meta.acknowledgments)
