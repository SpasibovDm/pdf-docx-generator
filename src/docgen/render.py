from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

def render_template(template_path: str, data: dict) -> str:
    tpath = Path(template_path)
    env = Environment(
        loader=FileSystemLoader(str(tpath.parent)),
        autoescape=select_autoescape(disabled_extensions=("j2",), default=False),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(tpath.name)
    return template.render(**data).strip() + "\n"
