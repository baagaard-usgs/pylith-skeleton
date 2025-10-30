import journal


class Informational(journal.info, active=True, fatal=False):
    """Pylith info journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
