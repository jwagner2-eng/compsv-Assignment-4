# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# 7. First Repeated Value
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    seen = set()

    for value in values:
        if value in seen:
            return value
        seen.add(value)

    return None


# Test cases
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # Expected: 3
print(first_repeated_value([1, 2, 3, 4]))              # Expected: None
print(first_repeated_value([]))                         # Expected: None
print(first_repeated_value([5, 5, 6, 7]))              # Expected: 5
print(first_repeated_value(["a", "b", "c", "b"]))       # Expected: b
