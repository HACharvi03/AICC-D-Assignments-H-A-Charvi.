import numpy as np

temps = [28, 32, 40, 37, 26, 38]

# Convert to numpy array
arr = np.array(temps)

print("Array:", arr)
print("Max Temp:", np.max(arr))
print("Min Temp:", np.min(arr))
print("Average Temp:", np.mean(arr))

# Last 3 days temperature
print("Last 3 days:", arr[-3:])