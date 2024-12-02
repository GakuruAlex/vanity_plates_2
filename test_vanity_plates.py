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

#Test for is_int_in_mid
@pytest.mark.parametrize("plate, is_valid", [
    ("AAA222", False),
    ("AA22AA", True),
    ("AA2A22", True),
    ("AAA022", True),
    ("AAA200", False),
    ("AA02A2", True),
    ("AA02AA", True)
])
class TestIsIntInMiddle:
    plates = Plates()
    def test_is_int_in_middle(self, plate, is_valid):
        assert self.plates.is_int_in_mid(plate) == is_valid

#Test contains_punctuation
@pytest.mark.parametrize("plate, is_valid", [
    ("AAA 222", False),
    ("AAA222", True),
    ("AAA22@", False),
    ("AAA.AA", False)
])
class TestContainsPunctuation:
    plates = Plates()
    def test_contains_no_punctuation(self, plate, is_valid):
        assert self.plates.contains_no_punctuation(plate) == is_valid

#Test if the plate is valid

@pytest.mark.parametrize("plate, is_valid", [
    ("CS50", True),
    ("CS05", False),
    ("CS50P", False),
    ("PI3.14", False),
    ("H", False),
    ("OUTATIME", False),
    ("22222", False),
    ("HH", True)
])
class TestIsValid:
    plates = Plates()
    def test_is_valid(self, plate, is_valid):
        assert self.plates.is_valid(plate) == is_valid