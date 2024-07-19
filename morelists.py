class slider:

    def __call__(self, *args, **kwargs):
        return self.__list

    def __init__(self, *args):
        self.__list = list(args)

    def __str__(self):
        return f"{self.__list}"

    def __getitem__(self, index: (int, slice)):
        if isinstance(index, slice):
            slice_format = self.__get_format_slice(index)

            return self.__list[slice_format]

        return self.__list[index % len(self.__list)]

    def __setitem__(self, index: int, value):
        self.__list[index % len(self.__list)] = value

    def __add__(self, other: (list, object)):
        return slider(*(self.__list + self.__isarray(other)))

    def __mul__(self, other):
        return self.__list * self.__isarray(other)

    def __eq__(self, other) -> bool:
        return self.__list == self.__isarray(other)

    def __get_format_slice(self, slce: slice) -> slice:
        slice_format = [
            arg % len(self.__list) if arg != None
            else None for arg in [slce.start, slce.stop, slce.step]
        ]

        return slice(*slice_format)

    @classmethod
    def __isarray(cls, other):
        if isinstance(other, cls):
            return other.__list

        return other