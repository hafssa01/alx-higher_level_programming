#!/usr/bin/python3
"""Define write_file function with two arguments"""



def write_file(filename="", text=""):
    """Writes in filename"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
