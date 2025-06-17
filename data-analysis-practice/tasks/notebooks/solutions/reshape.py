from typing import List, Tuple
import numpy as np

def reshape_array(A, target_dimensionality, target_shape_requirements):
    shape = [1] * target_dimensionality
    total_elements = A.size
    
    if target_shape_requirements:
        # Calculate the product of the sizes specified in the requirements
        specified_product = int(np.prod([size for _, size in target_shape_requirements]))
        
        # Calculate the remaining elements
        remaining_elements = total_elements // specified_product
    else:
        remaining_elements = total_elements

    # Fill the unspecified dimensions with the remaining elements
    for i in range(target_dimensionality):
        if all(i != dim for dim, _ in target_shape_requirements):
            shape[i] = remaining_elements
            break

    # Update the dimensions specified in the requirements
    for dim, size in target_shape_requirements:
        shape[dim] = size

    return A.ravel().reshape(shape)