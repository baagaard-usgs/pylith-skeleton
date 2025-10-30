import pylith


class Debug(pylith.shells.command, family="pylith.cli.debug"):
    """Display debugging information about this application."""

    full = pylith.properties.bool(default=True)
    full.doc = "Display the full configuration."

    @pylith.export(tip="Print the application configuration namespace.")
    def config(self, plexus, **kwds):
        """Generate a list of encountered configuration files."""
        lines = []
        cfg = self.pyre_configurator
        for uri, priority in cfg.sources:
            lines += [f"{uri}, priority '{priority.name}'"]
        plexus.info.log("\n".join(lines))

        if self.full:
            plexus.info.report(plexus.pyre_showConfiguration(deep=True))
            plexus.info.log()
        return 0
