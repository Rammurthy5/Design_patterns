"""
This is part of Behavioural Design pattern. Intent is to have a abstract class as base, and a template method declared
 inside with a series of calls to the different steps defined inside.
 The steps may or not be abstract. Derived classes should choose the steps, and modify them if needed, but cant modify
 template method in base class.
 http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html

..date..     March 22nd 2020
..real-time eg..    https://refactoring.guru/design-patterns/template-method

"""

from abc import ABC, abstractmethod


class BaseCls(ABC):

    def templated(self):
        """
        Template method which shows the directives of how the steps gonna be implemented.
        :return: None
        """

        self.data = self.open()

        if self.data:
            return self.process_data()

    @abstractmethod
    def open(self):
        """ Step method. Can have default implementation or abstracted"""
        pass

    def process_data(self):
        """ Step method. Can have default implementation or abstracted"""
        return len(self.data)


class Derive1(BaseCls):

    def __init__(self, fp):
        self.file_path = fp

    def open(self):
        """Overriding Step method"""

        with open(self.file_path) as fp:
            return fp.read()

d = Derive1('singleton_design.py')
print(d.templated())
