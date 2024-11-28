import numpy as np

def swap(coords: np.ndarray):
    """
    This method will flip the x and y coordinates in the coords array.
    
    :param coords: A numpy array of bounding box coordinates with shape [n, 5] in format:
        [[x1, y1, x2, y2, classid1],
         [x2, y2, x3, y3, classid2],...]
    
    :return: The new numpy array where the x and y coordinates are flipped.
    """
    # Swap x1 with y1 and x2 with y2
    coords[:, [0, 1]] = coords[:, [1, 0]]
    coords[:, [2, 3]] = coords[:, [3, 2]]
    return coords

# Example usage
coords = np.array([[10, 5, 15, 6, 0],
                   [11, 3, 13, 6, 0],
                   [5, 3, 13, 6, 1],
                   [4, 4, 13, 6, 1],
                   [6, 5, 13, 16, 1]])

swapped_coords = swap(coords)
print(swapped_coords)
