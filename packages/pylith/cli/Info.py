import pylith


class Info(pylith.shells.command, family="pylith.cli.info"):
    """Display helpful information about the installed application."""

    @pylith.export(tip="Print information about the host computer.")
    def host(self, plexus, **kwds):
        """Print information about the host computer."""
        host = self.pyre_host

        info = pylith.journal.info_factory.about()
        lines = (
            f"name: {host.hostname}",
            f"nickname: {host.nickname}",
            f"tag: {host.tag}",
            f"os: {host.distribution} {host.release} ({host.codename})",
            f"arch: {host.cpus.architecture}",
            f"cores: {host.cpus.cores}",
        )
        info.report(lines)
        info.log()

    @pylith.export(tip="Print information PyLith dependencies.")
    def dependencies(self, plexus, **kwds):
        """Print information about PyLith dependencies."""
        raise NotADirectoryError(":TODO:")
