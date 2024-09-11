from typing import List

from pydantic import BaseModel


class NumList(BaseModel):
    nums: List[int]