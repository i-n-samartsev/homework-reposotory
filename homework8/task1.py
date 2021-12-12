"""
We have a file that works as key-value storage, each line is represented
as key and value separated by = symbol, example:

name=kek last_name=top song_name=shadilay power=9001

Values can be strings or integer numbers. If a value can be treated both as
a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as
attributes. Example:
storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay'
storage.power # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when
there's a line 1=something) ValueError should be raised. File size is expected
to be small, you are permitted to read it entirely into memory.
"""


class KeyValueStorage:
    """
        Wrapper class for key value storage.

        storage = KeyValueStorage('path_to_file.txt')

        File works as key-value storage, each line is represented as key and
        value separated by = symbol, example:

        name=kek
        last_name=top
        song_name=shadilay
        power=9001

        Keys and values accessible as collection items and as attributes:

        storage.name == 'kek'
        storage['power'] == 9001
    """
    def __init__(self, file: str):
        self.file = file
        self.__set_attrs_from_file()

    def __set_attrs_from_file(self):
        with open(self.file, mode='r') as file:
            for line in file:
                key, value = line.strip().split(sep='=')
                self.__setattr__(key, value)

    def __setattr__(self, key, value):
        value = int(value) if value.isdigit() else value
        if hasattr(self, key):
            pass
        elif key.isidentifier():
            object.__setattr__(self, key, value)
        else:
            raise ValueError(f'{key=} is invalid identifier')

    def __getitem__(self, item):
        try:
            return self.__getattribute__(item)
        except AttributeError:
            raise KeyError(item)
