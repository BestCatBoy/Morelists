class slider:

    def __call__(self, *args, **kwargs):
        return self.__list

    def __init__(self, *args):
        self.__list = self.__isstr(list(args))

    def __str__(self):
        try:
            return "".join(self.__list)
        except:
            return f"{self.__list}"

    def __getitem__(self, index: (int, slice)):
        if isinstance(index, slice):
            slice_format = self.__get_format_slice(index)
            return self.__list[slice_format]

        return self.__list[index % len(self.__list)]

    def __setitem__(self, index: int, value):
        self.__list[index % len(self.__list)] = value

    def __delitem__(self, index: int):
        del self.__list[index % len(self.__list)]

    def __add__(self, other: (list, object)):
        return slider(*(self.__list + self.__isslider(other)))

    def __mul__(self, other):
        return self.__list * self.__isslider(other)

    def __eq__(self, other) -> bool:
        return self.__list == self.__isslider(other)

    def __set__(self):
        return set(self.__list)

    def __get_format_slice(self, slce: slice) -> slice:
        slice_format = [
            arg % len(self.__list) if arg != None
            else None for arg in [slce.start, slce.stop, slce.step]]
        return slice(*slice_format)

    def append(self, item):
        self.__list.append(item)

    def split(self, sep = None):
        try:
            self.__list = "".join(self.__list)
            self.__list = self.__list.split(sep)
            return self.__list
        except:
            raise ArithmeticError("non- 'str' object has no attribute 'split'")

    @classmethod
    def __isslider(cls, obj):
        if isinstance(obj, cls):
            return obj.__list

        return obj

    @classmethod
    def __isstr(cls, obj):
        if (len(obj) == 1) and (isinstance(obj[0], str)):
            obj = list(obj[0])

        return obj

## append +
## split +
## reverse -
## insert
## pop