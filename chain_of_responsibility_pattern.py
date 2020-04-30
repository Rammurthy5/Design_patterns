"""
Creates a series simple Handler type classes before reaching the final business logic layer. works like chain connected
to each other, can move further only if current handler pass you through, otherwise exit away.

..date..    March 26, 2020
..real-time eg..    you have different level of authorizations for each registered user in your app, you dont want to
                    let everybody access all things. Set different layer of validation layers 'Handlers' technically to
                     solve this.

https://refactoring.guru/design-patterns/chain-of-responsibility/python/example#lang-features
"""

from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass


class BaseHandler(Handler):

    _instance: Handler = None

    def set_next(self, handler):
        self._instance = handler
        if self._instance:
            return self._instance

    def handle(self, request):
        if self._instance:
            return self._instance.handle(request)

        return None


class MonkeyHandler(BaseHandler):

    def handle(self, request):
        if request == 'banana':
            return f"{self.__class__.__name__} can have the {request}"
        else:
            return super().handle(request)


class BirdHandler(BaseHandler):

    def handle(self, request):
        if request == 'seeds':
            return f"{self.__class__.__name__} can have the {request}"
        else:
            return super().handle(request)


class CatHandler(BaseHandler):

    def handle(self, request):
        if request == 'milk':
            return f"{self.__class__.__name__} can have the {request}"
        else:
            return super().handle(request)


class MouseHandler(BaseHandler):

    def handle(self, request) -> str:
        if request == 'cake':
            return f"{self.__class__.__name__} can have the {request}"
        else:
            return super().handle(request)


monkey = MonkeyHandler()
cat = CatHandler()
mouse = MouseHandler()
bird = BirdHandler()

monkey.set_next(cat).set_next(bird).set_next(mouse)


def food_splitter(handler: Handler) -> None:

    food = ['banana', 'milk', 'cake', 'seeds']

    for _ in food:
        print(f"Who wants {_}")
        response = handler.handle(_)

        if response:
            print(response)
        else:
            print(f"{_} left untouched")


food_splitter(monkey)

food_splitter(cat)
