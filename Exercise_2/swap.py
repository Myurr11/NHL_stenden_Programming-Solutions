import numpy as np

def swap(coords: np.ndarray) -> np.ndarray:
    """
    Swaps the x and y coordinates in the coords array.
    """
    # Create a copy of the array to avoid overwriting
    swapped_coords = coords.copy()
    
    # Swap x and y coordinates
    swapped_coords[:, 0] = coords[:, 1]  # y11 -> x11
    swapped_coords[:, 1] = coords[:, 0]  # x11 -> y11
    swapped_coords[:, 2] = coords[:, 3]  # y12 -> x12
    swapped_coords[:, 3] = coords[:, 2]  # x12 -> y12
    
    return swapped_coords

# Example Usage
coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])
swapped_coords = swap(coords)
print(swapped_coords)
