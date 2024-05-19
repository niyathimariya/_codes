# 283. Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for x in range(0,len(nums)):
            if nums[x]==0:
                temp=nums[x]
                nums.remove(nums[x])
                nums.append(temp)
        return nums
solution = Solution()
nums=[0,1,0,3,12]
print(solution.moveZeroes(nums))