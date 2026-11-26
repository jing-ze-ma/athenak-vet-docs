# Sphinx configuration. Layout, theme and settings follow the IAS AthenaK documentation
# (https://github.com/IAS-Astrophysics/athenak-docs), which this site is modelled on.
from __future__ import annotations

project = "AthenaK VET radiation"
author = "Jing-Ze Ma, Claude Opus 5.5 and AthenaK contributors"
copyright = "2026, Jing-Ze Ma, Claude Opus 5.5 and AthenaK contributors"
release = "vet-clean-release"

extensions = [
    "sphinx.ext.mathjax",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "AthenaK VET radiation documentation"

# footer of every page: link to the release code
RELEASE_URL = "https://github.com/jing-ze-ma/athenak/tree/vet-clean-release"
html_theme_options = {
    "footer_icons": [
        {
            "name": "Release code on GitHub",
            "url": RELEASE_URL,
            "html": "Release code: github.com/jing-ze-ma/athenak",
            "class": "",
        },
    ],
}

# links checked by `make linkcheck`: internal only (the code and gallery repos may be private)
linkcheck_ignore = [r"https?://"]
