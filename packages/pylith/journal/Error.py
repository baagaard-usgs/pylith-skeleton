import journal


class Error(journal.error, active=True, fatal=True):
    """Pylith error journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
