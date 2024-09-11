from typing import List


class Solution:
    @staticmethod
    def check_Duplicate(nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
