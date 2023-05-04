# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
__version__='2023.1'

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UIBCDF - Talleres'
copyright = '2023, UIBCDF Lab at the Mexico City Childrens Hospital Federico Gomez and authors.'
author = 'Liliana M. Moreno Vargas & Diego Prada Gracia. <a href="mailto:uibcdf@gmail.com">Contact us</a>.'

version = __version__.split('+')[0]
release = __version__



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.githubpages',
#    'sphinxcontrib.bibtex',
    'sphinx.ext.extlinks',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_favicon',
    'myst_nb',
]

# Myst extensions and options

myst_enable_extensions = [
    'dollarmath',
    'amsmath',
    'colon_fence'
]

myst_heading_anchors = 3

# Autosummary options

autosummary_generate = True

# Napoleon settings
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_use_param = False
napoleon_use_ivar = True

# sphinxcontrib-bibtex
#bibtex_bibfiles = ['bibliography.bib'] # list of *.bib files
#bibtex_default_style = 'alpha'
#bibtex_encoding = 'utf-8-sig'

# Add any paths that contain templates here, relative to this directory.

templates_path = ['_templates']
exclude_patterns = []

source_parsers={
}

source_suffix = ['.md', '.ipynb']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# language was edited to use sphinx-intl
language = 'es'

# These next two variables were incluede to use sphinx-intl
locale_dirs =  ['_locale/']
gettext_compact = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
#html_theme = 'pydata_sphinx_theme'
html_theme_options = {
            "logo": {"alt_text": "UIBCDF-Talleres"},

}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []

html_static_path = ['_static']
html_logo = "_static/LogoUIBCDF_vertical.png"

favicons = ["favicon-16x16.png",
            "favicon-124x124.png",
            "favicon-128x128.png",
            "favicon-192x192.png",
            "icon.svg"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# Custom css

html_css_files = [
    'custom.css',
]

