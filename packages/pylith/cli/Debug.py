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
        info = pylith.journal.info_factory.debug_config()
        info.report(lines)

        if self.full:
            info.report(plexus.pyre_showConfiguration(deep=True))
        info.log()
        return 0
