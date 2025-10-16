"""
focuses on constructing a simple immutable object, 
like a user profile, with several optional fields. 
This best illustrates why the pattern is needed—to handle many optional parameters without complex,
 hard-to-read constructors.

real-world applications include:
- Configuring complex objects like database connections or network requests.
- Building UI components with various optional settings.    

"""

# 1. Product (The complex object)
class User:
    def __init__(self, name, age=None, email=None, is_verified=False):
        self.name = name
        self.age = age
        self.email = email
        self.is_verified = is_verified

    def __str__(self):
        details = [f"Name: {self.name}"]
        if self.age is not None:
            details.append(f"Age: {self.age}")
        if self.email is not None:
            details.append(f"Email: {self.email}")
        details.append(f"Verified: {self.is_verified}")
        return ", ".join(details)

# 2. Concrete Builder
class UserBuilder:
    def __init__(self, name):
        # Mandatory field set in the Builder's constructor
        self._name = name
        # Optional fields initialized to None or default
        self._age = None
        self._email = None
        self._is_verified = False

    def set_age(self, age):
        self._age = age
        return self  # Return self for method chaining (Fluent API)

    def set_email(self, email):
        self._email = email
        return self

    def verify(self):
        self._is_verified = True
        return self

    def build(self):
        # The final step that creates and returns the immutable User object
        return User(
            name=self._name,
            age=self._age,
            email=self._email,
            is_verified=self._is_verified
        )

# Client Usage
# Building a fully configured user
user1 = UserBuilder("Alice").set_age(30).set_email("alice@example.com").verify().build()
print(f"User 1: {user1}")

# Building a minimally configured user
user2 = UserBuilder("Bob").set_age(25).build()
print(f"User 2: {user2}")