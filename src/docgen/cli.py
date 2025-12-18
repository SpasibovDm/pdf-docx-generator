import json
from pathlib import Path
import argparse

from docgen.render import render_template
from docgen.pdf import make_pdf
from docgen.docx_out import make_docx

def main():
    ap = argparse.ArgumentParser(description="Generate PDF/DOCX from JSON + Jinja2 template")
    ap.add_argument("--data", required=True, help="Path to JSON data")
    ap.add_argument("--template", default="templates/anschreiben_de.j2", help="Path to .j2 template")
    ap.add_argument("--outdir", default="output", help="Output directory")
    ap.add_argument("--name", default="anschreiben", help="Base output filename without extension")
    args = ap.parse_args()

    data = json.loads(Path(args.data).read_text(encoding="utf-8"))
    rendered = render_template(args.template, data)

    outdir = Path(args.outdir)
    pdf_path = outdir / f"{args.name}.pdf"
    docx_path = outdir / f"{args.name}.docx"

    make_pdf(rendered, str(pdf_path), signature_image=data.get("signature_image"))
    make_docx(rendered, str(docx_path))

    print(f"OK: {pdf_path}")
    print(f"OK: {docx_path}")

if __name__ == "__main__":
    main()
