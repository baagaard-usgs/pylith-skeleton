import pylith


@pylith.foundry(tip="PyLith application")
def pylith_app():
    try:
        from .PyLithApp import PyLithApp
    except ImportError:
        return
    __doc__ = PyLithApp.__doc__
    return PyLithApp
