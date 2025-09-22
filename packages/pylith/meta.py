date = "2025-09-20"
major = 6
minor = 0
micro = 0


version = (major, minor, micro)

copyright = "Copyright (c) 2005-2025 all rights reserved"

banner = f"""
    PyLith v{major}.{minor}.{micro}
    {copyright}
"""


authors = """
    Brad T. Aagaard, USGS, USA
    Mathew G. Knepley, University at Buffalo, USA
    Charlies A. Williams, Earth Science New Zealand, New Zealand
"""

acknowledgments = """"""

header = banner + authors

license = (
    header
    + """
license:
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions
    are met:

    * Redistribution of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistribution in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in
      the documentation and other materials provided with the
      distribution.

    * Neither the name qed nor the names of its contributors may be
      used to endorse or promote products derived from this software
      without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
    FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
    INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
    BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
    LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
    ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
"""
)

citations = {
    "software": {
        "type": "@manual",
        "key": "pylith:software",
        "title": f"PyLith Version {major}.{minor}.{micro}",
        "author": "Aagaard, B. and Knepley, M. and Williams, C.",
        "organization": "Computational Infrastructure for Geodynamics (CIG)",
        "address": "University of California, Davis",
        "year": f"{date[0:4]}",
        "doi": "",
    },
    "manual": {
        "type": "@manual",
        "key": "pylith:manual",
        "title": f"PyLith Version {major}.{minor}.{micro}",
        "author": "Aagaard, B. and Knepley, M. and Williams, C.",
        "organization": "Computational Infrastructure for Geodynamics (CIG)",
        "address": "University of California, Davis",
        "year": f"{date[0:4]}",
        "note": f"https://pylith.readthedocs.io/en/v{major}.{minor}.{micro}",
    },
    "article-XX": {
        "type": "@article",
        "key": "pylith:software",
        "title": "",
        "author": "Aagaard, B. and Knepley, M. and Williams, C.",
        "organization": "Computational Infrastructure for Geodynamics (CIG)",
        "address": "University of California, Davis",
        "year": "",
        "doi": "",
    },
}
