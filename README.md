# pdf-docx-generator (Python)

Generate **PDF & DOCX** documents from structured **JSON** using **Jinja2 templates**.
Useful for automating German job applications (Anschreiben), contracts and other repetitive documents.

## Features
- JSON → Jinja2 → rendered text
- Export to **PDF (ReportLab)** and **DOCX (python-docx)**
- Optional signature image embedding
- Simple CLI usage

## Tech Stack
Python · Jinja2 · ReportLab · python-docx

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python src/docgen/cli.py \
  --data examples/anschreiben.sample.json \
  --template templates/anschreiben_de.j2 \
  --outdir output \
  --name anschreiben_demo
