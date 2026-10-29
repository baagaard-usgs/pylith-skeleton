# =================================================================================================
# This code is part of PyLith, developed through the Computational Infrastructure
# for Geodynamics (https://github.com/geodynamics/pylith).
#
# Copyright (c) 2010-2026, University of California, Davis and the PyLith Development Team.
# All rights reserved.
#
# See https://mit-license.org/ and LICENSE.md and for license information.
# =================================================================================================

import yaml

import journal

import pylith


def channels():
    """Build the roster of journal channels the GUI offers.

    Each entry is a {(severity, name)} pair drawn from the {journal.channels} list in
    {pylith_app.yaml}. The severities that the live journal does not recognize are dropped,
    so a typo in the configuration cannot reach the schema.

    :TODO: retrieve the channels at runtime from the configuration store, via
    {journal.channels}, rather than parsing {pylith_app.yaml} directly, once the running
    Pyre app's configuration store is reachable from the resolver.
    """
    # the configured channels, deduplicated while keeping the order they appear in
    roster = []
    seen = set()
    # go through the pairs the configuration lists
    for severity, name in _configured():
        # the identity of the channel
        channel = (severity, name)
        # skip a severity the journal does not know, and a channel already on the roster
        if severity not in journal.severities or channel in seen:
            continue
        # remember it
        seen.add(channel)
        # and add it
        roster.append(channel)
    # hand back the roster
    return roster


def _configured():
    """Read the {(severity, name)} pairs from the {journal.channels} list in {pylith_app.yaml}.

    Each list item is a string of the form {"severity, name"}; a malformed item is skipped.
    """
    # the configuration file
    path = _configpath()
    # if there is no copy to read
    if path is None:
        # note it on a channel of its own
        channel = journal.warning("pylith.gql.journal")
        channel.line("could not find 'pylith_app.yaml'")
        channel.line("the journal channel roster is empty")
        channel.log()
        # the roster is empty
        return
    # attempt to read and parse it
    try:
        # open it
        with open(str(path)) as stream:
            # and parse it
            document = yaml.safe_load(stream)
    # if it cannot be read
    except OSError as error:
        # note it on a channel of its own
        channel = journal.warning("pylith.gql.journal")
        channel.line(f"could not read the journal channels from '{path}'")
        channel.line(f"got: {error}")
        channel.log()
        # the roster is empty
        return
    # the {journal.channels} list, if the document has one
    entries = (document or {}).get("journal", {}).get("channels", [])
    # go through the entries
    for entry in entries:
        # split a {"severity, name"} string on its comma
        severity, _, name = str(entry).partition(",")
        # tidy up the pieces
        severity = severity.strip()
        name = name.strip()
        # a well-formed entry has both
        if severity and name:
            # hand it over
            yield severity, name
    # all done
    return


def _configpath():
    """Locate {pylith_app.yaml}, or nothing if neither copy is present.

    The installed configuration lives in the package's share directory ({pylith.defaults});
    a build run from the source tree reads it from {etc/pylith} under the package home.
    """
    # the candidate directories, in the order they are preferred
    candidates = []
    # the installed share directory, if the package found its prefix
    if pylith.defaults is not None:
        # holds the configuration
        candidates.append(pylith.defaults / "pylith_app.yaml")
    # the source tree copy sits in {etc/pylith}, two levels above {packages/pylith}
    candidates.append(pylith.home.parent.parent / "etc" / "pylith" / "pylith_app.yaml")
    # go through them
    for path in candidates:
        # and take the first that is there
        if path.isFile():
            # found it
            return path
    # neither copy is present
    return None


# End of file
