# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'balancr'
copyright = '2022, balancr'
author = 'balancr'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []
extensions = ['sphinx.ext.autosectionlabel']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

#-- Define a global variable rst_prolog ------
# https://stackoverflow.com/questions/10870719/inline-code-highlighting-in-restructuredtext

rst_prolog = """
.. role:: python(code)
    :language: python
    :class: highlight
.. role:: bash(code)
    :language: bash
    :class: highlight
"""

