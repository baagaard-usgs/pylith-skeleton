# access the framework
import pyre


# protocol declaration
class Action(pyre.action, family="pylith.cli"):
    """
    Protocol declaration for pylith commands
    """
