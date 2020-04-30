"""
The objective is to learn and implement Singleton Design Pattern in Python.

..real-time-example..   Can be applied wherever we want to restrict the instantiation of the class to once.
..Date..                14th March 2020
..author..              Rammurty Subrahmaniyan
"""


class _TestSingleton:

    __instiante_flag = False
    _single = False

    def __new__(cls, *args, **kwargs):

        if not cls.__instiante_flag:
            cls.__instiante_flag = True
            return object.__new__(cls)

        return "already instantiated. cant do it again! Get out"


t = _TestSingleton()
print(t)

t2 = _TestSingleton()
print(t2)


# Eg 2  using metaclasses.


class check(type):

    _instance = None

    def __call__(self, *args, **kwargs):
        print("called")
        if not self._instance:
            self._instance = super().__call__()

        return self._instance


class CC(metaclass=check):

    pass



c = CC()
d = CC()

print(id(c), id(d))     # shows same ID. singleton achieved.

