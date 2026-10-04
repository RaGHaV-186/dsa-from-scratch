"""
Problem: 1929. Concatenation of Array (Easy)
Pattern: Array basics
Idea: (1) nums + nums. (2) Pre-fill 2n slots, write nums[i] to i and i+n in one pass.Time:    O(n)  (builds a list of 2n items; drop the constant)
Space:   O(n) for the output, O(1) extra
Mistake: Forgot to state space complexity at first.
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

    def getConcatenationLoop(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)          # 2n empty slots
        for i in range(n):
            ans[i] = nums[i]         # first half
            ans[i + n] = nums[i]     # mirrored second half
        return ans


# ---------- tests ----------
if __name__ == "__main__":
    s = Solution()

    assert s.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert s.getConcatenation([5]) == [5, 5]   # edge case: n = 1
    assert s.getConcatenationLoop([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenationLoop([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert s.getConcatenationLoop([5]) == [5, 5]

    print("All tests passed")