# Cryptnox ID CLI

[![PyPI](https://img.shields.io/pypi/v/cryptnox-id-cli.svg)](https://pypi.org/project/cryptnox-id-cli/)
[![Python versions](https://img.shields.io/pypi/pyversions/cryptnox-id-cli.svg)](https://pypi.org/project/cryptnox-id-cli/)
[![docs](https://github.com/embarquech/cryptnox-id-cli/actions/workflows/docs.yml/badge.svg)](https://github.com/embarquech/cryptnox-id-cli/actions/workflows/docs.yml)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

Command-line management for the [Cryptnox ID](https://docs.cryptnox.com/cryptnox-id/)
card family. One tool for all three card functions:

* **PIV** — SP 800-73 identity credentials (keys + X.509 certificates)
* **FIDO2 / CTAP 2.1** — passkeys / WebAuthn
* **MIFARE DESFire** — contactless applications (incl. EV3 Secure Dynamic Messaging)

Full documentation: **https://docs.cryptnox.com/cryptnox-id-cli/**

## Requirements

* Python 3.10+
* A PC/SC stack: built into Windows and macOS; on Linux install `pcscd` +
  `libccid`.
* A PC/SC reader. MIFARE DESFire needs a DESFire-capable *contactless* reader.

## Install

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .\.venv\Scripts\Activate.ps1
pip install cryptnox-id-cli
cryptnox-id --version
```

Three interchangeable console commands are installed: `cryptnox-id`, the short
`cnx-id`, and `cryptnox-id-card`.

## First run

```bash
cryptnox-id readers     # list readers, card presence, ATR
cryptnox-id info        # detect the card + all functions on one screen
cryptnox-id doctor      # PC/SC service, reader, per-function reachability
cryptnox-id shell       # interactive prompt (run subcommands without the prefix)
```

`info` and `doctor` are read-only and safe to run any time. From there, follow a
quick start in the [documentation](https://docs.cryptnox.com/cryptnox-id-cli/):
PIV, FIDO2, or MIFARE.

## Platform notes

* **FIDO2 on Windows** needs an Administrator terminal — Windows reserves the
  CTAP interface for its WebAuthn API. Linux and macOS have no such restriction.
* **PIV administration** is contact-only.
* **MIFARE DESFire** requires a reader that passes native DESFire commands
  (ACS ACR1252 verified).

## Development

```bash
pip install -e ".[dev]"
ruff check src tests && ruff format --check src tests
mypy
pytest -q -m "not real_card"
```

Unit tests use a mock transport — no reader or card required. Real-card tests are
opt-in (`-m real_card`) and never run in CI.

## Documentation

The docs are built with Sphinx. Warnings are fatal (`-W`), matching CI.

```bash
pip install -r docs/requirements.txt
```

Build the HTML site (output in `docs/_build/html/`):

```bash
cd docs
make html
# open docs/_build/html/index.html
```

Push to `main` deploys the site to GitHub Pages.

## License

This project is available under the GNU **LGPL v3** (see [`LICENSE`](LICENSE)). A
commercial license is also available — see [`COMMERCIAL.md`](COMMERCIAL.md). The
documentation is licensed CC BY-NC-ND 4.0.
