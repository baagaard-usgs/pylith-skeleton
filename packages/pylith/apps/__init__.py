import pylith


@pylith.foundry(tip="PyLith application")
def pylith_app(**kwds):
    from .PyLithApp import PyLithApp
    __doc__ = PyLithApp.__doc__
    if kwds:
        return PyLithApp(**kwds)
    return PyLithApp
