# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'PPTeam_Template'
copyright = '2024, E.C.Bunschoten'
author = 'E.C.Bunschoten'

# The full version, including alpha/beta/rc tags
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.autodoc'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Options for latex documentation. Include packages and define environments and
# variables under 'extrapackages' and 'preamble'.
latex_engine='xelatex'

latex_elements={'fontpkg': r'''
\setmainfont{Times New Roman}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
\setlength{\abovecaptionskip}{0pt}
\definecolor{cverbbg}{HTML}{F0E68C}''',
'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
'printindex': r'\footnotesize\raggedright\printindex',
'extrapackages' : r'''\usepackage{siunitx}
\usepackage{todonotes}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage{fancyvrb,newverbs,xcolor}'''
}