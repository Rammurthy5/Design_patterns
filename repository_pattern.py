"""
acts as an intermediary layer between the domain (business logic) layer of 
an application and the data mapping layer (like an ORM or raw database queries). 
Its purpose is to centralize data access logic, making the domain layer 
independent of the specific data storage technology.

.. real-world e.g., Microservice Architecture that needs to support multiple, evolving data storage solutions.
"""

from abc import ABC, abstractmethod

# 1. Domain Model (The object the application uses)
class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# 2. Repository Interface (Abstract Base Class)
class UserRepository(ABC):
    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def update(self, user: User):
        pass

# 3. Concrete Repository (Implementation using an in-memory dictionary)
class InMemoryUserRepository(UserRepository):
    def __init__(self):
        # Data storage specific to this concrete implementation
        self._users = {}
        self._next_id = 1

    def add(self, user: User):
        # Assign a new ID and store the user
        user.id = self._next_id
        self._users[user.id] = user
        self._next_id += 1
        print(f"InMemory: Added user {user.name} with ID {user.id}")

    def get_by_id(self, user_id: int) -> User:
        return self._users.get(user_id)

    def update(self, user: User):
        if user.id in self._users:
            self._users[user.id] = user
            print(f"InMemory: Updated user {user.id}")
        else:
            print(f"InMemory: User ID {user.id} not found for update.")

# Client/Application Layer Usage
# The application layer only interacts with the abstract interface.

# Initialize the repository (choosing the implementation)
user_repo = InMemoryUserRepository()

# Create
new_user = User(None, "Alice", "alice@corp.com")
user_repo.add(new_user)
alice_id = new_user.id

# Read
retrieved_user = user_repo.get_by_id(alice_id)
print(f"Retrieved: {retrieved_user}")

# Update
retrieved_user.email = "alice.new@corp.com"
user_repo.update(retrieved_user)

# Read after update
print(f"Updated: {user_repo.get_by_id(alice_id)}")