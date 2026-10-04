"""
Problem: 1929. Concatenation of Array (Easy)
Pattern: Array basics
Idea:    Answer is the list followed by itself, so return nums + nums.
Time:    O(n)  (builds a list of 2n items; drop the constant)
Space:   O(n) for the output, O(1) extra
Mistake: Forgot to state space complexity at first.
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums


# ---------- tests ----------
if __name__ == "__main__":
    s = Solution()

    assert s.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert s.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert s.getConcatenation([5]) == [5, 5]   # edge case: n = 1

    print("All tests passed")