class Solution:
    def binarySearch(self, arr, low, high, x):
        if high >= low:
            mid = low + (high - low) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] > x:
                return self.binarySearch(arr, low, mid-1, x)

            else:
                return self.binarySearch(arr, mid + 1, high, x)

        else:
            return -1

solution = Solution()
arr = [2, 3, 4, 10, 40]
x = 10
result = solution.binarySearch(arr, 0, len(arr)-1, x)
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")

    

    
    



