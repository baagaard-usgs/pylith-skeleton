import journal


class Help(journal.help):
    """Pylith help journal."""

    def record(self):
        self.notes["application"] = self.name
        return super().record()
