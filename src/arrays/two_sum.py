from typing import List

def twosum( nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        # print(f"for i= {i} and num= {num}")
        complement = target-num    # 9-num
        # print(f"compliment= {complement}")
        if(complement in seen):
            # print(seen[complement], i)
            return [seen[complement],i]
        seen[num] = i
        # print(seen)
    return[]