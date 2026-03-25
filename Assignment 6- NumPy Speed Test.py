import time
import numpy as np

size = 1_000_000

start_time = time.time()

py_list = list(range(size))
py_result = [x * 2 for x in py_list]  

end_time = time.time()
list_time = end_time - start_time

print("Python List Time:", list_time, "seconds")

start_time = time.time()

np_array = np.arange(size)
np_result = np_array * 2  

end_time = time.time()
numpy_time = end_time - start_time

print("NumPy Array Time:", numpy_time, "seconds")