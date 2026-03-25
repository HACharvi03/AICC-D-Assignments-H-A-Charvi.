Netflix-like Recommendation:
It checks what movies you watched
Finds users with similar taste
Recommends movies those similar users liked

Dataset (User Ratings)
User	Action	Comedy	Drama
A	      5	      1	      2
B	      4	      2	      1
C	      1	      5	      4
You	      5	      1	      ?


import numpy as np

# Data: [Action, Comedy]
A = np.array([5, 1])
B = np.array([4, 2])
C = np.array([1, 5])
You = np.array([5, 1])

# Distance function
def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

# Compute distances
dist_A = distance(You, A)
dist_B = distance(You, B)
dist_C = distance(You, C)

print("Distance with A:", dist_A)
print("Distance with B:", dist_B)
print("Distance with C:", dist_C)

# Find nearest neighbor
nearest = min([(dist_A, "A"), (dist_B, "B"), (dist_C, "C")])
print("Nearest User:", nearest[1])

# Drama ratings
drama_ratings = {"A": 2, "B": 1, "C": 4}

print("Recommended Drama Rating:", drama_ratings[nearest[1]])