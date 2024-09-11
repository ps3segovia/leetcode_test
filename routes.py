from fastapi import APIRouter

from core import Solution
from models import NumList

router = APIRouter()

@router.post("/check_duplicates")
def check_duplicates(data: NumList):
    result = Solution.check_Duplicate(data.nums)
    return result



