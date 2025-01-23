"""
Word counter CLI tool.
"""

import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def main(
    file_name: str = None,
    count_lines: Annotated[bool, typer.Option("--lines", "-l")] = False,
    count_words: Annotated[bool, typer.Option("--words", "-w")] = False,
    count_bytes: Annotated[bool, typer.Option("--characters", "-c")] = False,
):
    """Main function for the script."""
    output: str = ""
    with open(file_name, encoding="utf-8") as f:
        file_content = f.read()
        lines = file_content.split("\n")
        words = file_content.split()

        if not count_lines and not count_words and not count_bytes:
            count_lines = count_words = count_bytes = True

        if count_lines:
            output = f"{len(lines)} "

        if count_words:
            output = output + f"{len(words)} "

        if count_bytes:
            byte_count = len(file_content)
            output = output + f"{byte_count}"

    typer.echo(f"{output.strip()} {file_name}")


if __name__ == "__main__":
    app()
