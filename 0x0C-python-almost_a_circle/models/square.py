#!/usr/bin/python3
# square.py
"""Defines the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle
    Args:
        size, x=0, y=0, id=None
    Raisses:
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Intiates the square object
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of the square object
        """

        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self._Rectangle__x,
                                                 self._Rectangle__y,
                                                 self._Rectangle__width)

    @property
    def size(self):
        """returns the size of the object
        """

        return self._Rectangle__width

    @size.setter
    def size(self, size):
        """sets the new width and height
        """

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """

        new_args = [self.id,
                    self._Rectangle__width,
                    self._Rectangle__x, self._Rectangle__y]
        if len(args) == 0 or args is None:
            if len(kwargs) == 0:
                return
            else:
                try:
                    new_args[0] = kwargs['id']
                except KeyError:
                    pass
                try:
                    new_args[1] = kwargs['size']
                except KeyError:
                    pass
                try:
                    new_args[2] = kwargs['x']
                except KeyError:
                    pass
                try:
                    new_args[3] = kwargs['y']
                except KeyError:
                    pass
        else:
            for x in range(len(args)):
                if x < len(new_args):
                    new_args[x] = args[x]
        self.__init__(new_args[1],
                      new_args[2],
                      new_args[3],
                      new_args[0])

    def to_dictionary(self):
        """Returns a dictionary representation of the the
        object"""

        obj_dic = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return obj_dic
