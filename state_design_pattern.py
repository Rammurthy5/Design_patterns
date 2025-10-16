"""
allows an object to alter its behavior when its internal state changes. 
The object appears to change its class. It's often used to eliminate large, 
unwieldy conditional statements (like if-elif-else or switch cases) that depend on the object's state.

The pattern has 3 main components:
1. Context: The object whose behavior changes (e.g., a door, a player, an order).
2. State Interface: Defines a common interface for all concrete states.
3. Concrete States: Classes that implement the state interface and define the specific behavior for that state.

real-world e.g.: traffic light system, vending machine.
"""

from abc import ABC, abstractmethod

# 1. State Interface (Abstract Base Class)
class LightState(ABC):
    @abstractmethod
    def handle(self, context):
        """Handle the state change and transition to the next state."""
        pass

# 2. Concrete States
class RedLight(LightState):
    def handle(self, context):
        print("🔴 Traffic Light is RED. Vehicles must STOP.")
        # Transition to the next state
        context.set_state(GreenLight())

class GreenLight(LightState):
    def handle(self, context):
        print("🟢 Traffic Light is GREEN. Vehicles may GO.")
        # Transition to the next state
        context.set_state(YellowLight())

class YellowLight(LightState):
    def handle(self, context):
        print("🟡 Traffic Light is YELLOW. Vehicles must PREPARE TO STOP.")
        # Transition to the next state
        context.set_state(RedLight())

# 3. Context
class TrafficLight:
    def __init__(self, initial_state: LightState):
        self._state = initial_state

    def set_state(self, new_state: LightState):
        print(f"Context: Transitioning from {type(self._state).__name__} to {type(new_state).__name__}")
        self._state = new_state

    def change(self):
        # Delegate the specific behavior to the current state object
        self._state.handle(self)

# Client Usage
print("--- Starting Traffic Cycle ---")
traffic_light = TrafficLight(RedLight())

traffic_light.change() # Should go from Red -> Green
print("-" * 20)
traffic_light.change() # Should go from Green -> Yellow
print("-" * 20)
traffic_light.change() # Should go from Yellow -> Red