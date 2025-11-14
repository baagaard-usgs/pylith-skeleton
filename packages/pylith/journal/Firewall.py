import journal


class Firewall(journal.firewall):
    """Pylith firewall journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
