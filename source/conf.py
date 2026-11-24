# Sphinx configuration. Layout, theme and settings follow the IAS AthenaK documentation
# (https://github.com/IAS-Astrophysics/athenak-docs), which this site is modelled on.
from __future__ import annotations

project = "AthenaK VET radiation"
author = "Jing-Ze Ma and AthenaK contributors"
copyright = "2026, Jing-Ze Ma and AthenaK contributors"
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

# links checked by `make linkcheck`: internal only (the code and gallery repos may be private)
linkcheck_ignore = [r"https?://"]
