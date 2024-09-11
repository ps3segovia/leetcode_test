from typing import List


class Solution:
    @staticmethod
    def check_Duplicate(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[nums[i]] = i
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in num_dict and num_dict[difference] != i:
                return [i, num_dict[difference]]