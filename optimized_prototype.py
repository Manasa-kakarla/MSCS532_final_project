import numpy as np
import time

# Function to compute the sum using a standard Python list
def sum_with_list(size):
    """
    Computes the sum of integers from 0 to size-1 using a standard Python list.

    Parameters:
    size (int): The size of the list to be created.

    Returns:
    int: The sum of the integers.
    """
    data = list(range(size))  # Creating a list from 0 to size-1
    total = 0
    for value in data:
        total += value  # Summing the values
    return total

# Function to compute the sum using a NumPy array
def sum_with_numpy(size):
    """
    Computes the sum of integers from 0 to size-1 using a NumPy array.

    Parameters:
    size (int): The size of the NumPy array to be created.

    Returns:
    int: The sum of the integers.
    """
    data = np.arange(size)  # Creating a NumPy array from 0 to size-1
    return np.sum(data)      # Efficient sum operation using NumPy

# Size of the dataset
data_size = 10**7  # Set to 10 million for performance testing

# Measure performance of the Python list
start_time = time.time()  # Record start time
list_sum = sum_with_list(data_size)  # Compute sum with list
list_duration = time.time() - start_time  # Calculate duration

# Measure performance of the NumPy array
start_time = time.time()  # Record start time
numpy_sum = sum_with_numpy(data_size)  # Compute sum with NumPy
numpy_duration = time.time() - start_time  # Calculate duration

# Display the results
print(f"Sum using list: {list_sum}, Duration: {list_duration:.4f} seconds")
print(f"Sum using NumPy: {numpy_sum}, Duration: {numpy_duration:.4f} seconds")
