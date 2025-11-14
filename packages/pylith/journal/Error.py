import journal


class Error(journal.error):
    """Pylith error journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
