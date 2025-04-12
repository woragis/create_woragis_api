# create_woragis_api/main.py

import click
import shutil
from pathlib import Path

TEMPLATES = ["rest", "grpc", "ai-rest", "ai-grpc", "mixed", "ai-mixed"]


@click.command()
@click.argument("template", type=click.Choice(TEMPLATES, case_sensitive=False))
@click.option("--output", "-o", default=".", help="Where to scaffold the project.")
def cli(template, output):
    """Scaffold a FastAPI backend with the given template."""
    template = template.lower()
    src = Path(__file__).parent / "templates" / template
    dst = Path(output).resolve()

    if not src.exists():
        click.echo(f"❌ Template '{template}' not found.")
        return

    click.echo(f"🚀 Scaffolding project with '{template}' template into {dst}")
    shutil.copytree(src, dst, dirs_exist_ok=True)

    click.echo("\n✅ Done!")
    click.echo(
        f"\n📦 To install dependencies:\n  pip install create_woragis_api[{template}]")
