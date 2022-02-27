import pyre
from pyre.units.mass import kg
from pyre.units.time import s
from pyre.units.length import m

from ObserverInjector import Observer,Injector

class Material(pyre.protocol, family="pylith.materials"):
    """Protocol declarator for materials.
    """

    #observer = Observer()
    #observer.doc = "Observer of material state."

    @classmethod
    def pyre_default(cls, **kwds):
        """The default {Material} implementation
        """
        return Elasticity

    @pyre.provides
    def initialize(self):
        """Initialize material.
        """

    @pyre.provides
    def setState(self, t):
        """Set material state.
        """

    @pyre.provides
    def computeState(self, t):
        """Compute material state.
        """

    @pyre.provides
    def finalState(self, t):
        """Set material end state.
        """
        self.observer.update(t)


class Elasticity(pyre.component, family="pylith.materials.elasticity", implements=Material):
    """Elasticity material behavior.
    """

    observer = Observer()
    observer.doc = "Observer of material state."

    density = pyre.properties.dimensional(default=3000*kg/m**3)
    density.doc = "Mass density."

    vp = pyre.properties.dimensional(default=5200.0*m/s)
    vp.doc = "P wave speed."

    vs = pyre.properties.dimensional(default=3000.0*m/s)
    vs.doc = "S wave speed."

    @pyre.export
    def initialize(self):
        """Initialize material.
        """
        print(f"Elasticity material '{self.pyre_name}'")
        print("\n".join(list(self.pyre_showConfiguration())))

    @pyre.export
    def setState(self, t):
        """Set material state.
        """
        print(f"Setting state for elasticity material '{self.pyre_name}'...")

    @pyre.export
    def computeState(self, t):
        """Compute material state.
        """
        print(f"Computing state for elasticity material '{self.pyre_name}'...")

    @pyre.export
    def finalState(self, t):
        """Set material end state.
        """
        self.observer.update(t)


class IncompressibleElasticity(pyre.component, family="pylith.materials.incompressibleelasticity", implements=Material):
    """Incompressible elastic material behavior.
    """

    density = pyre.properties.dimensional(default=3000*kg/m**3)
    density.doc = "Mass density."

    vs = pyre.properties.dimensional(default=5200.0*m/s)
    vs.doc = "S wave speed."

    @pyre.export
    def initialize(self):
        """Initialize material.
        """
        print(f"Incompressible elasticity material '{self.pyre_name}'")
        print("\n".join(list(self.pyre_showConfiguration())))

    @pyre.export
    def setState(self, t):
        """Set material state.
        """
        print(f"Setting state for incompressible elasticity material '{self.pyre_name}'...")

    @pyre.export
    def computeState(self, t):
        """Compute material state.
        """
        print(f"Computing state for incompressible elasticity material '{self.pyre_name}'...")

    @pyre.export
    def finalState(self, t):
        """Set material end state.
        """
        return


class InjectMaterial(pyre.component, family="pylith.injectors.material"):
    """Inject value into material state.
    """

    target = Material()
    target.doc = "Material to inject value into."
    
    value = pyre.properties.float(default=2.0)
    value.doc = "Value to inject."
    
    @pyre.export
    def setState(self):
        """Update state.
        """
        self.target.setState(self.value)

        
class Transfer(pyre.component, family="pylith.transfer", implements=(Observer,Injector)):
    """Transfer state from one object to another.
    """

    target = Material()
    target.doc = "Material to inject value into."
    
    def __init__(self, **kwds):
        """Constructor."""
        super().__init__(**kwds)
        self.t = None
    
    @pyre.export
    def update(self, t):
        """Update observer.
        """
        self.t = t
        self.setState()

    @pyre.export
    def setState(self):
        """Update state.
        """
        self.target.setState(self.t)


# end of file
