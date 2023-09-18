#!/usr/bin/python3

class Base:
    """
    Base class for managing object IDs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The ID to assign to the object. If not provided, an incremented ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

