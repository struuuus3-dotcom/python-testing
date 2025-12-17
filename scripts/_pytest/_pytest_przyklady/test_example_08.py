# Wbudowane fikstury pytest - caplog
import pytest
import logging


def save_file(filename):
    """Function that logs messages"""
    logging.info(f"Saving file: {filename}")
    logging.warning(f"File {filename} already exists")
    return True


def test_caplog_captures_logs(caplog):
    """caplog - przechwytuje wiadomości z logging"""
    
    caplog.set_level(logging.INFO)
    save_file("test.txt")

    assert "Saving file: test.txt" in caplog.messages
    assert "File test.txt already exists" in caplog.messages

    assert "test.txt" in caplog.text
