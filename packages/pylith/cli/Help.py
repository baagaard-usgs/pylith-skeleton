import pyre

import pylith


class Help(pylith.shells.command, family="pyre.cli.help"):
    """Display help information for this application."""

    @pyre.export(tip="Print links to documentation.")
    def resources(self, plexus, **kwds):
        from pylith import meta

        manual_url = (
            f"https://pylith.readthedocs.io/en/v{meta.major}.{meta.minor}.{meta.micro}"
        )
        tutorials_url = "https://geodynamics.org/courses/PyLith"
        forum_url = "https://community.geodynamics.org/c/pylith"

        lines = (
            "Before you ask for help, consult the PyLith user manual and try to debug on your own.",
            "You will likely find other useful information while making progress resolving your original issue.",
            "",
            "PyLith User Resources",
            f"    - Manual: {manual_url}",
            f"    - Tutorials: {tutorials_url}",
            f"    - Community forum: {forum_url}",
            "",
            "When submitting a question to the PyLith forum about running a simulation, be sure to include",
            "1. Describe what you are trying to do",
            "    a. Overview of the problem and boundary conditions (diagrams are very helpful)",
            "    b. Cell type (tri, quad, hex, or tet)",
            "    c. Type of fault: prescribed slip or spontaneous rupture",
            "2. Indicate which version of PyLith you are using.",
            "3. Send the *entire* error message, not just what you think is important (entire log is best).",
        )
        plexus.info.log("\n".join(lines))

    @pyre.export(tip="Print the documentation for an object.")
    def object_docs(self, plexus, **kwds):
        """Print documentation for an object."""
        raise NotImplementedError(":TODO:")
