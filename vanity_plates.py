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
        """_Checks if a digit is in the middle of letters and that the first digit is not a zero_

        Args:
            plate (str): _Requested plate_

        Returns:
            bool: _True if plate has digit between letters and first digit is not zero else False_
        Example:
            >>> is_int_in_mid("AA2AA2")
            True
            >>> is_int_in_mid("AAA222")
            False
        """
        for index,char in enumerate(plate):
            if char.isdigit():
                new_plate =plate[index:]
                break
        return any(char.isalpha() for char in new_plate) or int(new_plate[0]) == 0
    def contains_no_punctuation(self, plate: str)-> bool:
        """_Check if plate contains punctuation and spaces_

        Args:
            plate (str): _Requested plate_

        Returns:
            bool: _True if no punctuation and spaces else False_
        Example:
            >>> contains_no_punctuation("AAAAA")
            True
            >>> contains_no_punctuation("PI3.14")
            False
        """
        return plate.isalnum()
    def is_valid(self, plate: str)-> bool:
        """_Check if the plate is valid i.e has valid length, no puctuactions , starts with two letters and no digits in the middle of letters_

        Args:
            plate (str): _Requested plate_

        Returns:
            bool: _True if plate is valid else False_
        
        Example:
            >>> is_valid("AAA222")
            True
            >>> is_valid("Hello World")
            False
            >>> is_valid("AAA020")
            False
            >>> is_valid("22222")
            False
        """
        if self.is_length_valid(plate):
            if self.is_plate_alphanum(plate):
                return not self.is_int_in_mid(plate) and self.starts_with_two_letters(plate) and self.contains_no_punctuation(plate)
            elif plate.isalpha():
                return self.contains_no_punctuation(plate)
            else:
                return False
        else:
            return False