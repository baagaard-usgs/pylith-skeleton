import journal


class Informational(journal.info):
    """Pylith info journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
