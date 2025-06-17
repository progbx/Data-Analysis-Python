from typing import List, Tuple
import numpy as np


def reshape_array(input_array: np.ndarray, target_dimensionality: int, target_shape_requirements: List[Tuple[int, int]]) -> np.ndarray:
    """Reshapes a given ndarray according to the given requirements.

    `target_shape_requirements` is a list of <axis_index; value> pairs, meaning that `result.shape[axis_index] == value` is required. 

    Args:
        input_array: np.ndarray, the array to reshape
        target_dimensionality: int, the required dimensionality of the resulting array
        target_shape_requirements: List[Tuple[int, int]], a list of requirements for the shape of the resulting array
    Returns:
        np.ndarray, the resulting array
    """
    # Create a shape with appropriate dimensionality
    new_shape = [1] * target_dimensionality
    
    # Apply the requirements
    for axis_index, value in target_shape_requirements:
        new_shape[axis_index] = value
    
    # Get total number of elements
    total_elements = input_array.size
    
    # Calculate the product of specified dimensions
    specified_product = 1
    for dim_size in new_shape:
        specified_product *= dim_size
    
    # Calculate how many elements remain to be distributed
    remaining_elements = total_elements // specified_product
    
    # Find the first dimension that isn't specified in requirements
    remaining_axes = [i for i in range(target_dimensionality) if i not in [ax for ax, _ in target_shape_requirements]]
    
    if remaining_axes:
        # Assign remaining elements to the first unspecified dimension
        new_shape[remaining_axes[0]] = remaining_elements
    
    # Reshape the array
    return input_array.reshape(new_shape)
