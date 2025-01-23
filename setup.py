from setuptools import setup

setup(
    name="word-counter",
    version="0.1.0",
    description="Word counter CLI tool.",
    long_description="Word counter CLI tool, written in python using typer.",
    py_modules=["main"],
    install_requires=["typer"],
    entry_points={
        "console_scripts": [
            "ccwc=main:app",
        ]
    },
)
