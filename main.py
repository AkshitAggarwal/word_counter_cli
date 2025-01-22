"""
Word counter CLI tool.
"""

import typer
from typing_extensions import Annotated

app = typer.Typer()


def main(
    file_name: str = None,
    count_lines: Annotated[bool, typer.Option("--lines", "-l")] = False,
    count_words: Annotated[bool, typer.Option("--words", "-w")] = False,
    count_characters: Annotated[bool, typer.Option("--characters", "-c")] = False,
):
    """Main function for the script."""
    output: str = ""
    with open(file_name, encoding="utf-8") as f:
        file_content = f.read()
        lines = file_content.split("\n")
        words = file_content.split()
        if count_lines:
            output = output + f"{len(lines)} lines"

        if count_words:
            output = output + f" {len(words)} words"

        if count_characters:
            output = output + f" {len(file_content)} characters"

    print(f"{output.strip()}.")


if __name__ == "__main__":
    typer.run(main)
