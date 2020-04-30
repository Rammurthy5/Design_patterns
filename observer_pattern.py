"""
The intent of this yet another behavior design pattern is to automatically notify all dependents when one of em updated
 or changes state.

..date..    March 22 2020.
..real-time eg..    A class has been acting as publisher and there are many subscriber classes available and waiting for
                    information. we dont want publisher to get to know about all those subscribers, & not want to create
                    a dependency with all of them. so we create an interface where publisher will communicate only through
                    that interface. all subscribers can connect to that interface.This interface should declare the
                    notification method along with a set of parameters that the publisher can use to pass some
                    contextual data along with the notification.

https://refactoring.guru/design-patterns/observer
"""

from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, observable, *args):
        pass


class Observable:

    def __init__(self):
        self.__observers = list()

    def add_observer(self, x):
        self.__observers.append(x)

    def delete_observer(self, x):
        self.__observers.remove(x)

    def notify_observers(self, *args):
        for _ in self.__observers:
            _.update(self, *args)


class Twitter(Observable, Observer):

    def __init__(self, x):
        super().__init__()
        self._name = x

    @property
    def name(self):
        return self._name

    def follow(self, new_follower):
        new_follower.add_observer(self)
        return self

    def tweet(self, content):
        self.notify_observers(content)

    def update(self, observable, tweet):
        print(f"{self.name} received a tweet from {observable.name}: {tweet}")


a = Twitter('Alice')
k = Twitter('King')
q = Twitter('Queen')
h = Twitter('Mad Hatter')
c = Twitter('Cheshire Cat')

a.follow(c).follow(h).follow(q)
k.follow(q)
q.follow(q).follow(h)
h.follow(a).follow(q).follow(c)

print(f'==== {q.name} tweets ====')
q.tweet('Off with their heads!')
print(f'\n==== {a.name} tweets ====')
a.tweet('What a strange world we live in.')
print(f'\n==== {k.name} tweets ====')
k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
print(f'\n==== {c.name} tweets ====')
c.tweet("We're all mad here.")
print(f'\n==== {h.name} tweets ====')
h.tweet('Why is a raven like a writing-desk?')