import journal


class Warning(journal.warning, active=True, fatal=False):
    """Pylith warning journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
