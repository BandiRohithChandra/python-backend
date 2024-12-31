from datetime import date
from typing import List

class Address:
    def __init__(self, street: str, city: str):
        self.street = street
        self.city = city
    
    def __repr__(self):
        return f"Address(street={self.street}, city={self.city})"


class ImmutableEmployee:
    def __init__(self, name: str, id: str, date_of_joining: date, addresses: List[Address]):
        self.name = name
        self.id = id
        self.date_of_joining = date_of_joining
        # Creating a copy of the list to ensure immutability of the addresses
        self._addresses = addresses.copy()

    # Getter for addresses to return a copy of the list
    @property
    def addresses(self):
        return self._addresses.copy()

    def __repr__(self):
        return (f"ImmutableEmployee(name={self.name}, id={self.id}, "
                f"date_of_joining={self.date_of_joining}, addresses={self._addresses})")

# Example usage
address1 = Address("123 Main St", "Springfield")
address2 = Address("456 Oak St", "Greenville")

employee = ImmutableEmployee(
    name="John Doe",
    id="E12345",
    date_of_joining=date(2020, 5, 1),
    addresses=[address1, address2]
)

print(employee)
print(employee.addresses)  # Will show the list of addresses

# Trying to change addresses or other attributes will raise errors
# employee.name = "Jane Doe"  # This will raise an AttributeError
