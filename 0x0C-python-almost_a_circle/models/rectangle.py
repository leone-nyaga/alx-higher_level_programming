#!/usr/bin/python3
"""
Module containing the Rectangle class.
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
            Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
            Defaults to 0.
            id (int, optional): The ID to assign to the rectangle.
            Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The width of the rectangle.

        Raises:
            ValueError: If value is not an integer or if it's less
            than or equal to 0.
        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The height of the rectangle.

        Raises:
            ValueError: If value is not an integer or if it's less than
            or equal to 0.
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the x attribute.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the x attribute.

        Args:
            value (int): The x-coordinate of the rectangle's position.

        Raises:
            ValueError: If value is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the y attribute.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the y attribute.

        Args:
            value (int): The y-coordinate of the rectangle's position.

        Raises:
            ValueError: If value is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates and returns area of the triangle

        Returns:
            int: Area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints Rectangle instance using '#' character to represent its shape
        """
        for _ in range(self.__height):
            print('#' * self.__width)

    def __str__(self):
        """
        Returns a string representation of the rectangle instance

        Returns:
            str: A string in the format "[Rectangle](<id>) <x>/<y> -
            <width>/<height>"
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def display(self):
        """
        Prints the Rectangle instance with '#' characters, considering x and y.

        The top-left position of the rectangle is shifted by (x, y).
        """
    for _ in range(self.__y):
        print()
    for _ in range(self.__height):
        print(' ' * self.__x + '#' * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to the attributes.

        Args:
            *args: Positional arguments in the order: id, width, height, x, y.
            **kwargs: Keyword arguments where each key represents an attribute.

        Note:
            **kwargs will be skipped if *args exists and is not empty.
        """
        if args:
            num_args = len(args)

            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

