import journal


class Firewall(journal.firewall, active=True, fatal=True):
    """Pylith firewall journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
