from typing import List

class Perfect_Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            c = target - n
            if c not in nums_dict:
                nums_dict[n] = i
                print(nums_dict)
            else:
                return [i, nums_dict[c]]
                print(nums_dict)
    

            
print(Perfect_Solution().twoSum(nums=[2,8,12,4,6,3,5,11,0,21,52,47, 7, 11, 15], target=9))
