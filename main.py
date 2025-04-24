import click
import shutil
from pathlib import Path

# Define templates and their corresponding extras paths
TEMPLATES = {
    "rest": {"template_path": "templates/rest", "extras_path": "extras/fastapi"},
    "grpc": {"template_path": "templates/grpc", "extras_path": "extras/fastapi"},
    "ai-rest": {"template_path": "templates/ai-rest", "extras_path": "extras/fastapi"},
    "ai-grpc": {"template_path": "templates/ai-grpc", "extras_path": "extras/fastapi"},
    "rest-grpc": {"template_path": "templates/rest-grpc", "extras_path": "extras/fastapi"},
    "ai-rest-grpc": {"template_path": "templates/ai-rest-grpc", "extras_path": "extras/fastapi"},
    "data-science": {"template_path": "templates/data-science", "extras_path": "extras/data-science"},
    "data-science-ml": {"template_path": "templates/data-science-ml", "extras_path": "extras/data-science"},
    "data-science-ml-ai": {"template_path": "templates/data-science-ml-ai", "extras_path": "extras/fastapi"},
}


@click.command()
@click.argument("template", type=click.Choice(list(TEMPLATES.keys()), case_sensitive=False))
@click.option("--output", "-o", default=".", help="Where to scaffold the project.")
def cli(template, output):
    """Scaffold a project with the given template."""
    # Convert template to lowercase to handle case-insensitivity
    template = template.lower()

    # Define the template and extras paths
    src = Path(__file__).parent / TEMPLATES[template]["template_path"]
    extras = Path(__file__).parent / TEMPLATES[template]["extras_path"]
    dst = Path(output).resolve()

    # Check if the template exists
    if not src.exists():
        click.echo(f"❌ Template '{template}' not found.")
        return

    # Check if the destination directory already exists
    if dst.exists():
        click.echo(
            f"❌ Directory '{dst}' already exists. Please choose a different output directory.")
        return

    # Scaffold the project with the selected template
    click.echo(f"🚀 Scaffolding project with '{template}' template into {dst}")
    shutil.copytree(src, dst, dirs_exist_ok=True)

    # Copy extras if they exist
    if extras.exists():
        click.echo(f"📦 Adding extras from {extras}...")
        extras_dst = dst / "extras"
        # Ensure the extras folder exists
        extras_dst.mkdir(parents=True, exist_ok=True)
        shutil.copytree(extras, extras_dst, dirs_exist_ok=True)

    click.echo("\n✅ Done!")
    click.echo(
        f"\n📦 To install dependencies:\n  pip install create_woragis_api[{template}]"
    )


if __name__ == "__main__":
    cli()
