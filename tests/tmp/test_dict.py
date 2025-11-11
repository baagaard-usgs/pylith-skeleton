#!/usr/bin/env python3

import pyre
from test import metadatas
import journal


class TestApp(pyre.application):
    """Application for running PyLith simulations."""

    ints = pyre.properties.dict(schema=pyre.properties.int())
    ints.doc = "Dictionary mapping str to int."

    objs = pyre.properties.dict(schema=metadatas.metadata())
    objs.doc = "Dictionary mapping str to Metadata."

    @pyre.export
    def main(self, *args, **kwds):
        if "y" in self.objs:
            print(f"self.objs['y']={self.objs['y']}, type={type(self.objs['y'])}")
        return 0


if __name__ == "__main__":
    app = TestApp(name="test.app")

    # set default journal parameters
    journal.decor(1)
    journal.detail(1)

    # Print out the application configuration
    channel = app.info
    # channel.activate()
    channel.report(app.pyre_showConfiguration(deep=True))
    channel.log()

    status = app.run()
    raise SystemExit(status)
