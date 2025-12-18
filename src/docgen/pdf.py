from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from pathlib import Path
import textwrap

def _draw_wrapped(c: canvas.Canvas, text: str, x: float, y: float, width_chars: int, leading: float):
    for line in text.splitlines():
        if not line.strip():
            y -= leading
            continue
        for wline in textwrap.wrap(line, width=width_chars, break_long_words=False):
            c.drawString(x, y, wline)
            y -= leading
    return y

def make_pdf(text: str, out_path: str, signature_image: str | None = None):
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(str(out), pagesize=A4)
    width, height = A4

    left = 20 * mm
    top = height - 20 * mm
    leading = 13
    c.setFont("Helvetica", 11)

    y = _draw_wrapped(c, text, left, top, width_chars=95, leading=leading)

    if signature_image:
        img_path = Path(signature_image)
        if img_path.exists():
            img_w = 45 * mm
            img_h = 18 * mm
            y_img = max(30 * mm, y + 2 * leading)
            c.drawImage(ImageReader(str(img_path)), left, y_img, width=img_w, height=img_h, mask="auto")

    c.showPage()
    c.save()
