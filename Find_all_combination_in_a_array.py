#TCS NQT
#[1,2,9]=[1,12,19,129,2,29]

def combination(a):
    combinations=[]
    combinations=a.copy();
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            































# def generate_combinations(arr):
#     # Helper function to generate permutations of a list
#     def permute(elements):
#         if len(elements) == 1:
#             return [elements]
#         permutations = []
#         for i in range(len(elements)):
#             # Get the current element
#             current = elements[i]
#             # Remaining elements
#             remaining = elements[:i] + elements[i+1:]
#             # Generate all permutations of the remaining elements
#             for p in permute(remaining):
#                 permutations.append([current] + p)
#         return permutations

#     # Helper function to generate combinations of a list
#     def combine(elements, length):
#         if length == 0:
#             return [[]]
#         if not elements:
#             return []
#         combinations = []
#         for i in range(len(elements)):
#             # Current element
#             current = elements[i]
#             # Remaining elements
#             remaining = elements[i+1:]
#             # Generate all combinations of remaining elements of length-1
#             for c in combine(remaining, length-1):
#                 combinations.append([current] + c)
#         return combinations

#     # Resultant set to store unique combinations
#     combinations_set = set()

#     # Include individual elements
#     for num in arr:
#         combinations_set.add(str(num))
    
#     # Generate combinations for all lengths
#     for length in range(2, len(arr) + 1):
#         for combo in combine(arr, length):
#             # Generate all permutations of the current combination
#             perms = permute(combo)
#             for perm in perms:
#                 # Join list elements to form numbers and sort digits
#                 number = ''.join(map(str, perm))
#                 sorted_number = ''.join(sorted(number))
#                 combinations_set.add(sorted_number)
    
#     return sorted(list(combinations_set), key=int)

# # Example usage
# arr = [1, 2, 9]
# combinations_list = generate_combinations(arr)
# print(combinations_list)
