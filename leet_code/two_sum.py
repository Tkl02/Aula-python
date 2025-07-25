from typing import List

# My solution
class MY_Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for r in range(len(nums)):
            for l in range(r):
                if nums[l] + nums[r] == target:
                    return [l, r]


# Great solution
class Perfect_Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            c = target - n
            if c not in nums_dict:
                nums_dict[n] = i
            else:
                return [i, nums_dict[c]]

# Select solutions

Solution = MY_Solution()
Solution = Perfect_Solution()

#use
result = Solution.twoSum(nums=[2, 7, 11, 15], target=9)
print(result)