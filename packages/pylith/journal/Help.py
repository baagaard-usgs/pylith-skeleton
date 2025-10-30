import journal


class Help(journal.info, active=True, fatal=False):
    """Pylith help journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
