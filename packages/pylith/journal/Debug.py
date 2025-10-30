import journal


class Debug(journal.debug, active=False, fatal=False):
    """Pylith debug journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
