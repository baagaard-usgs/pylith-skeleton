# -*- Python -*-
# -*- coding: utf-8 -*-
# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026 All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================
import pylith


class Run(pylith.shells.command, family="pyre.cli.run"):
    """Run the application."""

    @pylith.export(tip="generate completions candidates from a partial command line")
    def main(self, plexus, argv, **kwds):
        try:
            plexus.run_cxx()
        except pylith.exceptions.PyLithError:
            import pdb

            pdb.set_trace()
        return 0


# End of file
