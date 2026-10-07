"""
Problem : 217. Contains Duplicate
Pattern : Hash set (seen-set, early exit)
Idea    : Walk the array; if a number is already in the set, return True, else add it.
Time    : O(n), n = len(nums) — worst case all distinct
Space   : O(n) extra — values up to 10^9, no small cap
Mistake : First idea counted everything in a dict, but only "seen or not" matters, so a set + early exit is enough. Said "keys" when meaning the dict's values (counts).
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3, 4]) is False
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    print("all tests passed")