"""
Problem: 1480. Running Sum of 1d Array (Easy)
Pattern: Prefix sum
Idea:    Keep a running total `prev`; for each index, add nums[i] and store it.
Time:    O(n)
Space:   O(n) output, O(1) extra
Mistake:
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            prev += nums[i]
            ans[i] = prev
        return ans

# ---------- tests ----------
if __name__ == "__main__":
    s = Solution()

    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert s.runningSum([7]) == [7]              # edge: one element
    assert s.runningSum([5, -2, -3]) == [5, 3, 0]  # edge: negatives

    print("All tests passed")