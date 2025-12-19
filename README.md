# pdf-docx-generator (Python)

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Release](https://img.shields.io/github/v/release/SpasibovDm/pdf-docx-generator?label=release)

<details>
  <summary><b>Demo output (click to expand)</b></summary>

  <p align="center">
    <a href="assets/demo.png">
      <img src="assets/demo.png" width="350" alt="Demo output (PDF) preview">
    </a>
  </p>

  <p align="center">
    <a href="assets/demo.png">
      <img src="assets/demo.png" width="750" alt="Demo output (PDF) large">
    </a>
  </p>
</details>

## What it does

Generate **PDF & DOCX** documents from structured **JSON** using **Jinja2** templates.

**Use cases:**
- Job application letters (Anschreiben)
- Contracts / repetitive documents
- Any JSON → templated documents

## One-liner example (copy-paste)

```bash
PYTHONPATH=src python src/docgen/cli.py --data examples/anschreiben.sample.json --template templates/anschreiben_de.j2 --outdir output --name demo


## Project structure

src/docgen/     # generator (core logic + CLI)
templates/      # Jinja2 templates
examples/       # sample JSON data (no personal data)
assets/         # screenshots for README
output/         # generated locally (gitignored)
