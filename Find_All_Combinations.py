#TCS NQT
#[1,2,9]=[1,12,19,129,2,29]
from itertools import combinations

def generate_combinations(arr):
   
    combinations_set = set()
    for num in arr:
        combinations_set.add(str(num))

    for i in range(2, len(arr) + 1):
        for combo in combinations(arr, i):
            perms = set(permutations(combo))
            for perm in perms:
                number = ''.join(map(str, perm))
                sorted_number = ''.join(sorted(number))
                combinations_set.add(sorted_number)
    
    return list(combinations_set)

arr = [1, 2, 9]
combinations_list = generate_combinations(arr)
combinations_list = sorted(combinations_list, key=int)
print(combinations_list)
