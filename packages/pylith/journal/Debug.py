import journal


class Debug(journal.debug):
    """Pylith debug journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
