import pytest
from vanity_plates import Plates
@pytest.mark.parametrize("plate, is_valid", [
    ("AAA222", True),
    ("AA", True),
    ("A", False),
    ("1", False),
    ("1234567", False),
    ("AAABBBB", False),
    ("12345", True)
])
class TestIsLengthValid:
    """_Test whether is_valid function is correct_
    """
    plates = Plates()
    def test_is_length_valid(self, plate, is_valid):
        assert self.plates.is_length_valid(plate) == is_valid
    