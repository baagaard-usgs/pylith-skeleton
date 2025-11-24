# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2025, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


from ..protocols import application_metadata


class SimulationMetadata(
    pylith.component, implements=application_metadata, family="pylith.metadata.simulation_metadata"
):
    """Metadata for simulation.

    When using `base` to specify other files with metadata, the other files will append to the
    `keywords` and `features` lists, whereas other metadata will be overwritten
    (the same behavior as other Pyre properties).
    """

    description = pylith.properties.str(default=None)
    description.doc = "Description of this simulation."

    authors = pylith.properties.strings()
    authors.doc = "Creator(s) of this simulation."

    keywords = pylith.properties.strings()
    keywords.doc = "Keywords describing this simulation."

    features = pylith.properties.strings()
    features.doc = "PyLith features used in this simulation."

    arguments = pylith.properties.strings()
    arguments.doc = "Command line arguments for running this simulation."

    base = pylith.properties.strings()
    base.doc = "Parameter files with metadata that complement this metadata."

    version = pylith.properties.str()
    version.doc = "Version of this simulation."

    pylith_version = pylith.properties.strings()
    pylith_version.doc = "PyLith versions compatible with simulation input files."

    def __init__(self, name, locator, implicit, **kwds):
        """Constructor."""
        super().__init__(name, locator, implicit, **kwds)

        info = pylith.journal.info_factory.initialization()
        info.report(
            (
                f"{self}",
                f"description = {self.description}",
                f"authors = {self.authors}",
                f"keywords = {self.keywords}",
                f"features = {self.features}",
                f"arguments = {self.arguments}",
                f"base = {self.base}",
                f"version = {self.version}",
                f"PyLith version = {self.pylith_version}",
            )
        )
        info.log()

        todo = pylith.journal.debug_factory.todo()
        todo.report(("Implement SimulationMetadata.__init__(). Pass parameters to C++.",))
        todo.log()

    def pyre_initialized(self):
        errors = []

        todo = pylith.journal.debug_factory.todo()
        todo.log("Implement SimulationMetadata.pyre_initialized().")
        # from pylith.utils.utils import PylithVersion

        # version = PylithVersion.version()
        # major, minor, patch = version.split(".")
        # ok = True
        # for constraint in self.pylith_version:
        #     if not eval(f"{major}.{minor} {constraint}"):
        #         ok = False
        #         break
        # if not ok:
        #     trait = self.inventory.getTrait("pylith_version")
        #     self._validationError(
        #         context,
        #         trait,
        #         f"Installed PyLith version {version} does not meet" f" version constraints {self.pylith_version}.",
        #     )
        return errors


def from_file(filename):
    """Set simulation metadata from file.

    Args:
        filename (str)
            Name of file
    """
    todo = pylith.journal.firewall(":TODO:")
    todo.log("Implement SimulationMetadata.from_file().")

    metadata = None
    # def _get_properties(filename):
    #     """Get metadata from file."""
    #     if not os.path.isfile(filename):
    #         raise IOError(f"Could not open file '{filename}' to read metadata.")
    #     base, ext = os.path.splitext(str(filename))
    #     if ext == ".cfg":
    #         from pythia.pyre.inventory.cfg.CodecConfig import CodecConfig

    #         reader = CodecConfig()
    #     else:
    #         raise NotImplementedError(f"Reading '{ext}' file not implemented.")
    #     registry = reader.open(base)
    #     properties = None
    #     if registry and "inventory" in registry.keys() and "pylithapp" in registry["inventory"].facilities.keys():
    #         facilities = registry["inventory"].facilities["pylithapp"].facilities
    #         properties = facilities["metadata"].properties if "metadata" in facilities else None
    #         if properties:
    #             for key, descriptor in properties.items():
    #                 descriptor.value = CONVERTERS[key](descriptor.value)
    #     return properties

    # def _merge(target, source):
    #     """Merge properties.

    #     Args:
    #         target (dict)
    #             Object to update.
    #         source (dict)
    #             Object with data to use for update.
    #     """
    #     if not source:
    #         return
    #     APPEND = ["features", "keywords"]
    #     for key, descriptor in source.items():
    #         if descriptor.value:
    #             if key in APPEND:
    #                 assert isinstance(descriptor.value, list)
    #                 target[key].value += descriptor.value
    #             else:
    #                 target[key] = source[key]

    # metadata = None
    # properties = _get_properties(filename)
    # if properties:
    #     metadata = SimulationMetadata()
    #     if "base" in properties:
    #         base = properties["base"].value
    #         baseProperties = None
    #         for baseFilename in base:
    #             basePath = os.path.join(filename.parent, baseFilename)
    #             if not baseProperties:
    #                 baseProperties = _get_properties(basePath)
    #             else:
    #                 _merge(baseProperties, _get_properties(basePath))
    #         _merge(baseProperties, properties)
    #         properties = baseProperties

    #     for key, descriptor in properties.items():
    #         setattr(metadata, key, descriptor.value)
    return metadata
