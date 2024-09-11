from fastapi import APIRouter

from core import Solution
from models import NumList, Anagram, TwoSum, GroupAnagrams

router = APIRouter()


@router.post("/check_duplicates")
def check_duplicates(data: NumList):
    result = Solution.check_Duplicate(data.nums)
    return result


@router.post("/isAnagram")
def isAnagram(data: Anagram):
    result = Solution.isAnagram(data.s, data.t)
    return result


@router.post("/twoSum")
def twoSum(data: TwoSum):
    result = Solution.twoSum(data.nums, data.target)
    return result
@router.post("/group_anagrams")
def group_anagrams(data: GroupAnagrams):
    result = Solution.groupAnagrams(data.strs)
    return result