"""
Author: Akshit Aggarwal
Date: 21/01/2025
"""

import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command("words")
def word_count(file_name: str):
    """Prints the number of words in a file."""
    with open(file_name, encoding="utf-8") as f:
        words = f.read().split()
    print(f"File {file_name} has {len(words)} words.")


if __name__ == "__main__":
    app()
