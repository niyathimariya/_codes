#TCS NQT
#[1,2,9]=[1,12,19,129,2,29]
from itertools import combinations

from itertools import combinations, permutations

def generate_combinations(arr):
    # Resultant set to store unique combinations
    combinations_set = set()
    
    # Include individual elements
    for num in arr:
        combinations_set.add(str(num))
    
    # Generate combinations for all lengths
    for i in range(2, len(arr) + 1):
        for combo in combinations(arr, i):
            # Generate all permutations of the current combination
            perms = set(permutations(combo))
            for perm in perms:
                # Join tuple elements to form numbers and sort digits
                number = ''.join(map(str, perm))
                sorted_number = ''.join(sorted(number))
                combinations_set.add(sorted_number)
    
    return list(combinations_set)

# Example usage
arr = [1, 2, 9]
combinations_list = generate_combinations(arr)
combinations_list = sorted(combinations_list, key=int)
print(combinations_list)

