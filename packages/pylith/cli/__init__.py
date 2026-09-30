from ..shells import action

import pyre


# @foundry(implements=action, tip="A collection of introspection utilities.")
# def inspect():
#     from .Inspect import Inspect

#     __doc__ = Inspect.__doc__
#     return Inspect


@pyre.foundry(implements=action, tip="Information about this application.")
def about(**kwds):
    from .About import About
    __doc__ = About.__doc__
    if kwds:
        return About(**kwds)
    return About


@pyre.foundry(implements=action, tip="Help information for this application.")
def help(**kwds):
    from .Help import Help
    __doc__ = Help.__doc__
    if kwds:
        return Help(**kwds)
    return Help


@pyre.foundry(implements=action, tip="Configuration information.")
def config(**kwds):
    from .Config import Config
    __doc__ = Config.__doc__
    if kwds:
        return Config(**kwds)
    return Config


@pyre.foundry(implements=action, tip="Helpful information about the platform.")
def info(**kwds):
    from .Info import Info
    __doc__ = Info.__doc__
    if kwds:
        return Info(**kwds)
    return Info


@pyre.foundry(implements=action, tip="Debugging information.")
def debug(**kwds):
    from .Debug import Debug
    __doc__ = Debug.__doc__
    if kwds:
        return Debug(**kwds)
    return Debug


@pyre.foundry(implements=action, tip="Run application.")
def run(**kwds):
    from .Run import Run
    __doc__ = Run.__doc__
    if kwds:
        return Run(**kwds)
    return Run
