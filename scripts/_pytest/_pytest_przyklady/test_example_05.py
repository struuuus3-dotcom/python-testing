# Wbudowane fikstury pytest: request
import pytest
import os


def test_request_fixture(request):
    """request - metadane testu + cleanup functions"""

    # request.node - informacje o teście
    print(f"Test: {request.node.name}")

    # request.addfinalizer - cleanup (jak addCleanup)
    temp_file = "test_temp.txt"
    open(temp_file, "w").write("data")
    request.addfinalizer(lambda: os.remove(temp_file))

    assert os.path.exists(temp_file)
    # cleanup automatyczny po teście

# Żeby wyświetlić stdio nawet w przechodzących testach:
# pytest -s

# Bieżący parametry w sparametryzowanej fiksturze też dostępny z poziomu request.param
# def test_request_with_parametrized_fixture(fibonacci_number, request):
#     """Użycie request z parametryzowaną fixture"""
#     # request.param - aktualny parametr z fixture
#     current_param = request.param
#     print(f"Current fibonacci number: {current_param}")
#
#     assert current_param == fibonacci_number

#   request fixture:
#   - Metadane - informacje o teście, pliku, sesji
#   - Cleanup - addfinalizer() dla cleanup functions
#   - Parametry - request.param w parametryzowanych fixtures
#   - Kontrola - dostęp do konfiguracji pytest
