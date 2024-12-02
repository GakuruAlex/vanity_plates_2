class Plates:
    def is_length_valid(self, plate: str)-> bool:
        """_Check if the length of the plate is valid_

        Args:
            plate (str): _Requested car plate_

        Returns:
            bool: _True if the length of the plate is greater than one and less than seven_
        """
        return len(plate) > 1 and len(plate) < 7
    def starts_with_two_letters(self, plate: str)-> bool:
        """_A function to check if the first two characters of the plate are letter_

        Args:
            plate (str): _Requested plate_

        Returns:
            bool: _True if first two characters letters else False_
        """
        return plate[0:2].isalpha()
    def is_plate_alphanum(self, plate: str)->bool:
        """_Check if a plate contains both letters and numbers_

        Args:
            plate (str): _Requested plate_

        Returns:
            bool: _True if plate is alpha numerical otherwise False_
        """
        return any(char.isalpha() for char in plate)  and any(char.isdigit() for char in plate)
    def is_int_in_mid(self, plate: str)-> bool:
        pass
        