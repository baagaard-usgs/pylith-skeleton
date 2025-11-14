import journal


class Warning(journal.warning):
    """Pylith warning journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
