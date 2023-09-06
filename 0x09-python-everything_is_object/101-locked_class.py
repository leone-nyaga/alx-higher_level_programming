#!/usr/bin/python3
# 101-locked_class

class LockedClass:
    __slots__ = ('first_name',)

    def __setattr__(self, key, value):
        if key != 'first_name':
            raise AttributeError(f"Cannot set attribute '{key}' for LockedClass")
        self.__dict__[key] = value
