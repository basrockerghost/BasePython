import random
from collections import Counter

# Generate a list of random numbers
random_numbers = [random.randint(1, 10) for _ in range(100)]

# Count the occurrences of each number
counter = Counter(random_numbers)

# Print the random numbers and their counts
print("Random Numbers:", random_numbers)
print("Number Counts:", counter)
