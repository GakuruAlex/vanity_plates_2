class Plates:
    def is_length_valid(plate: str)-> bool:
        """_Check if the length of the plate is valid_

        Args:
            plate (str): _Requested car plate_

        Returns:
            bool: _True if the length of the plate is greater than two and less than seven_
        """
        return len(plate) > 2 and len(plate) < 7