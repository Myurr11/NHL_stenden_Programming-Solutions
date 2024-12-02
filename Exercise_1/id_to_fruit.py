def id_to_fruit(fruit_id: int, fruits: set[str]) -> str:
    """
    Returns the fruit name by getting the string at a specific index of the set, fixing the issue of unordered sets.
    """
    fruits_list = sorted(fruits)  # Convert set to sorted list
    if 0 <= fruit_id < len(fruits_list):
        return fruits_list[fruit_id]
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")

# Example Usage
name1 = id_to_fruit(1, {"apple", "orange", "melon", "kiwi", "strawberry"})  # 'kiwi'
name3 = id_to_fruit(3, {"apple", "orange", "melon", "kiwi", "strawberry"})  # 'orange'
name4 = id_to_fruit(4, {"apple", "orange", "melon", "kiwi", "strawberry"})  # 'strawberry'

print(name1, name3, name4)
