"""
The motive is to create a bridge class that can inter-link two incomptible classes.

..date..    March 22 2020.
..real-time eg..    we have a legacy product which sends out XML to our Python app which is deisgned to process XML, and
                    deliver the same. We want to integrate this processed XML data to a new 3rd party tool so that we
                    can find some analytics. But, the 3rd party tool accepts only Json format, and produces the same.
                    If we touch the existing Python app, it might break the app, so we are gonna write an adapter class
                    which will take XML as an input, and convert that into JSON input for 3rd party tool.
http://34.212.143.74/s201911/pycon2019/docs/design_patterns.html
https://refactoring.guru/design-patterns/adapter
"""

class Duck:

    def quack(self):
        print("quack quack")

    def fly(self):
        print("im flying")


class Turkey:

    def growl(self):
        print("growling")

    def fly(self):
        print("i can fly only a short distance")


def duck_interaction(duck):
    duck.quack()
    duck.fly()


duck = Duck()
turkey = Turkey()

duck_interaction(duck) # this works
# I want the immediate line of code to work without modifying anything in Duck / Turkey / duck_interaction classes & methods.
duck_interaction(Turkey)  # would obviously fail because we dont have quack() in Turkey class. thats why we need adapter


class AdapterTurkey:        # Adapter creation

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def quack(self):
        self.adaptee.growl()

    def fly(self):
        self.adaptee.fly()


turkey_adapter = AdapterTurkey(turkey)   # passing adaptee object, not class directly.

duck_interaction(turkey_adapter)   # this made the magic. Turkey now works with quack ;) 
