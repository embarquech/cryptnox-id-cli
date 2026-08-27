# Configuration file for the Sphinx documentation builder.
#
# This documentation set is the future public repo for the product docs,
# published like the other Cryptnox doc repos: GitHub Pages under
# https://docs.cryptnox.com/<repo_slug>/ and linked from the docs hub.

# -- Product identity: the ONLY lines to touch when the public name is decided --
product_name = "Cryptnox ID CLI"
repo_slug = "cryptnox-id-cli"
cli_name = "cryptnox-id"  # primary binary; cnx-id + cryptnox-id-card are aliases

# -- Hardware / shop links: single source of truth, edit here, used doc-wide via
#    the |reader-*| / |readers-link| substitutions (see rst_prolog below).
#    Names and shop links match the cryptnox-cli README. --
readers_url = "https://cryptnox.com/cardreaders/"
reader_contact_name = "Cryptnox Smartcard Reader"
reader_contact_url = "https://shop.cryptnox.com/product/cryptnox-smartcard-reader/"
reader_mini_name = "Compact USB Mini Smartcard Reader"
reader_mini_url = "https://shop.cryptnox.com/product/mini-smartcard-reader/"
reader_contactless_name = "Cryptnox NFC Contactless Reader"
reader_contactless_url = "https://shop.cryptnox.com/product/cryptnox-contactless-reader/"

project = product_name
author = "Cryptnox"
copyright = "2026, Cryptnox"  # noqa: A001 — footer format matches docs.cryptnox.com/cryptnox-cli
release = "0.1.0"  # keep in sync with the CLI release (see internal release checklist)
version = release

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.todo",  # draft markers on stub pages; never rendered (see below)
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = product_name
html_baseurl = f"https://docs.cryptnox.com/{repo_slug}/"
html_show_sphinx = False  # drop the "Built with Sphinx" footer line, matching docs.cryptnox.com/cryptnox-cli

# PDF output name for a local `make latexpdf` run. CI builds HTML only - pdflatex
# cannot render several characters these docs legitimately use.
latex_documents = [("index", f"{repo_slug}.tex", product_name, author, "manual")]

todo_include_todos = False  # .. todo:: blocks must never reach the published site

rst_prolog = f"""
.. |product| replace:: {product_name}
.. |cli| replace:: ``{cli_name}``
.. |readers-link| replace:: `Cryptnox card readers <{readers_url}>`__
.. |reader-contact| replace:: `{reader_contact_name} <{reader_contact_url}>`__
.. |reader-mini| replace:: `{reader_mini_name} <{reader_mini_url}>`__
.. |reader-contactless| replace:: `{reader_contactless_name} <{reader_contactless_url}>`__
"""
