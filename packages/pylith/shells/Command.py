import pyre

from .Action import Action as action


# class declaration
class Command(pyre.panel(), implements=action):
    """
    Base class for pylith commands
    """
