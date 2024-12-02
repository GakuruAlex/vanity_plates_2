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


#Test for starts_with_two_letters function

@pytest.mark.parametrize("plate, is_valid", [
    ("AAA222", True),
    ("222AAA", False),
    ("AA", True),
])
class TestStartsWithTwoLetters:
    plates = Plates()
    def test_starts_with_two_letters(self, plate, is_valid):
        assert self.plates.starts_with_two_letters(plate) == is_valid

#Test for is_plate_alphanum
@pytest.mark.parametrize("plate, is_valid", [
    ("AAA222", True),
    ("AAAAAA", False),
    ("22222", False),
    ("A", False),
    ("2", False),
    ("222AAA", True)
])
class TestIsPlateAlphaNumerical:
    plates = Plates()
    def test_is_alphanum(self, plate, is_valid):
        assert self.plates.is_plate_alphanum(plate) == is_valid