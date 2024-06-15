class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n):
            swapped = False

            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True

            if not swapped:
                break
# After the inner loop completes, the swapped flag is checked.If no swaps were made (swapped is False), it means the array is already sorted, and the outer loop is exited early to save unnecessary iterations.
        return arr

solution = Solution()
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = solution.bubbleSort(arr)
print("Sorted array:")
for i in range(len(sorted_arr)):
    print("%d" % sorted_arr[i], end=" ")
