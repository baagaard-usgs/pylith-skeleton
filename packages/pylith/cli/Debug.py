import pylith


class Debug(pylith.shells.command, family="pylith.cli.debug"):
    """Display debugging information about this application."""

    root = pylith.properties.str()
    root.default = None
    root.tip = "Specify the portion of the namespace to display."

    full = pylith.properties.bool(default=True)
    full.doc = "Display the full configuration."

    @pylith.export(tip="Generate a list of encountered configuration files.")
    def config(self, plexus, **kwds):
        """Generate a list of encountered configuration files."""
        lines = []
        cfg = self.pyre_configurator
        for uri, priority in cfg.sources:
            lines += [f"{uri}, priority '{priority.name}'"]
        info = pylith.journal.info_factory().debug_config()
        info.report(lines)

        if self.full:
            info.report(plexus.pyre_showConfiguration(deep=True))
        info.log()
        return 0

    @pylith.export(tip="Print the application configuration namespace.")
    def nfs(self, plexus, **kwds):
        """Print the application configuration namespace"""
        indent = " " * 2
        channel = pylith.journal.info_factory().debug_config()

        prefix = "pylith" if self.root is None else self.root
        nameserver = self.pyre_nameserver

        # get all nodes that match my {prefix}
        for info, node in nameserver.find(pattern=prefix):
            # attempt to
            try:
                value = node.value
            except nameserver.NodeError as error:
                # use the error message as the value
                value = f" ** ERROR: {error}"
            channel.line(f"{indent}{info.name}: {value}")

        channel.log()
        return 0

    @pylith.export(tip="Print the application virtual filesystem.")
    def vfs(self, plexus, **kwds):
        """Print the application virtual filesystem"""
        import pyre

        prefix = pyre.primitives.path("/pylith" if self.root is None else self.root)

        # starting at the root of the {vfs}
        folder = plexus.vfs
        # go through the {prefix} intermediate folder carefully
        for part in prefix.parts:
            try:
                folder = folder[part]
            except folder.NotFoundError:
                channel = pylith.journal.info_factory().debug_config()
                # complain
                channel.line(f"could not find '{part}' in '{folder.uri}'")
                channel.line(f"while scanning for '{prefix}' in the virtual file system")
                channel.log()
                # and bail if errors aren't fatal
                return 1
            # if the folder exists, get its contents
            folder.discover(levels=1)

        if self.full:
            folder.discover()

        report = folder.dump(indent=1)
        channel = pylith.journal.info_factory().debug_config()
        channel.line(f"vfs: prefix='{prefix}'")
        channel.report(report=report)
        channel.log()
        return 0
