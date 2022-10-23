"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Lightfeed."""


if __name__ == "__main__":
    main(prog_name="lightfeed")  # pragma: no cover
