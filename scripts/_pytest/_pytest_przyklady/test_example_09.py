# Wbudowane fikstury pytest - tmp_path

#   pathlib.Path API:
#   - / operator = łączenie ścieżek
#   - write_text() = tworzenie pliku z contentem
#   - read_text() = odczytywanie pliku
#   - exists() = sprawdzenie czy plik istnieje


def save_data(filepath, data):
    """Function that creates files"""
    filepath.write_text(data)
    return filepath.exists()


def test_tmp_path_creates_temp_directory(tmp_path):
    """tmp_path - automatyczny temporary directory (pathlib)"""

    test_file = tmp_path / "data.txt"

    result = save_data(test_file, "Hello World")

    assert result is True
    assert test_file.read_text() == "Hello World"
