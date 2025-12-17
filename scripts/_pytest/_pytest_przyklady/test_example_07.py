# Wbudowane fikstury pytest - capsys
import pytest


def print_user_info(name, age):
    """Function that prints to stdout - we want to test this output"""
    print(f"User: {name}")
    print(f"Age: {age}")
    print("Registration complete!")


def test_capsys_captures_stdout(capsys):
    """capsys - przechwytuje stdout/stderr do testowania"""

    print_user_info("John", 25)

    captured = capsys.readouterr()

    assert "User: John" in captured.out
    assert "Age: 25" in captured.out
    assert "Registration complete!" in captured.out

    assert captured.err == ""


def test_capsys_multiple_captures(capsys):
    """capsys można wywoływać wielokrotnie w jednym teście"""

    print("First output")
    first = capsys.readouterr()  # Pierwszy capture
    assert first.out == "First output\n"

    print("Second output")
    second = capsys.readouterr()  # Drugi capture
    assert second.out == "Second output\n"

    assert first.out != second.out


def test_capsys_with_stderr(capsys):
    """capsys przechwytuje też stderr"""
    import sys

    print("Normal output")
    print("Error message", file=sys.stderr)

    captured = capsys.readouterr()
    assert captured.out == "Normal output\n"
    assert captured.err == "Error message\n"
