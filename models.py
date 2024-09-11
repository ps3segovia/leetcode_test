from typing import List

from pydantic import BaseModel


class NumList(BaseModel):
    nums: List[int]


class Anagram(BaseModel):
    s: str
    t: str

class TwoSum(BaseModel):
    nums: List[int]
    target: int