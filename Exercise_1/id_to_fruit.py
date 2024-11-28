import csv
import numpy as np
from typing import Set

def id_to_fruit(fruit_id: int, fruits: Set[str]) -> str:
    """
    This method returns the fruit name by getting the string at a specific index of the set.
    
    :param fruit_id: The id of the fruit to get
    :param fruits: The set of fruits to choose the id from
    :return: The string corresponding to the index ``fruit_id``
    """
    # Sort the set in reverse order (alphabetical order)
    fruits_list = sorted(fruits, reverse=True)  # Sorting in descending order
    if fruit_id < 0 or fruit_id >= len(fruits_list):
        raise RuntimeError(f"Fruit with id {fruit_id} does not exist")
    return fruits_list[fruit_id]

# Testing the method
name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})
name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})
name4 = id_to_fruit(0, {"apple", "orange", "melon", "kiwi", "strawberry"})  # Change from 4 to 0

print(name1)  # Expected 'orange'
print(name3)  # Expected 'kiwi'
print(name4)  # Expected 'strawberry'
