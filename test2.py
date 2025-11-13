
from itertools import permutations

def generate_permutations_with_check(arr):
    n = len(arr)
    all_perms = list(permutations(arr))

    unique_perms = set()
    for perm in all_perms:
        if has_duplicates(perm):
            continue
        unique_perms.append(perm)

    return unique_perms



def has_duplicates(perm):
    seen = set()
    for element in perm:
        if element in seen:
            return True
        seen.add(element)
    return False


# Example usage
arr = [1, 2, 3, 4]
result = generate_permutations_with_check(arr)
print(f"Number of unique permutations: {len(result)}")
