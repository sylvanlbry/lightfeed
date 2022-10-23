"""Sphinx configuration."""
project = "Lightfeed"
author = "Sylvan St. Clair"
copyright = "2022, Sylvan St. Clair"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
