#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size (width/height) of the square.
            x (int, optional): The x-coordinate of the square's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the square's position.
            Defaults to 0.
            id (int, optional): The ID to assign to the square.
            Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the square instance

        Returns:
            str: A string in the format "[Square](<id>) <x>/<y> - <size>"
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

