from ..shells import action

import pyre


# @foundry(implements=action, tip="A collection of introspection utilities.")
# def inspect():
#     from .Inspect import Inspect

#     __doc__ = Inspect.__doc__
#     return Inspect


@pyre.foundry(implements=action, tip="Information about this application.")
def about():
    from .About import About

    __doc__ = About.__doc__
    return About


@pyre.foundry(implements=action, tip="Help information for this application.")
def help():
    from .Help import Help

    __doc__ = Help.__doc__
    return Help


@pyre.foundry(implements=action, tip="Configuration information.")
def config():
    from .Config import Config

    __doc__ = Config.__doc__
    return Config


@pyre.foundry(implements=action, tip="Helpful information about the platform.")
def info():
    from .Info import Info

    __doc__ = Info.__doc__
    return Info


@pyre.foundry(implements=action, tip="Debugging information.")
def debug():
    from .Debug import Debug

    __doc__ = Debug.__doc__
    return Debug


@pyre.foundry(implements=action, tip="Run application.")
def run():
    from .Run import Run

    __doc__ = Run.__doc__
    return Run
