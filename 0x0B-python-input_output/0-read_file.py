#!/usr/bin/python3
"""Defines file-reading function."""


def read_file(filename=""):
    """Reads filename with utf-8 and print its contents ."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
