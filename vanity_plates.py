class Plates:
    def is_length_valid(self,plate: str)-> bool:
        """_Check if the length of the plate is valid_

        Args:
            plate (str): _Requested car plate_

        Returns:
            bool: _True if the length of the plate is greater than one and less than seven_
        """
        return len(plate) > 1 and len(plate) < 7
    def starts_with_two_letters(plate: str) ->bool:
        """_A function to check if the first two characters of the plate are letter_

        Args:
            plate (str): _description_

        Returns:
            bool: _description_
        """