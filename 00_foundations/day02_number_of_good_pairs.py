"""
Problem : 1512. Number of Good Pairs
Pattern : Hash map (count seen so far)
Idea    : Each new number pairs with every equal number seen before it, so add its current count, then increment.
Time    : O(n), n = len(nums)
Space   : O(1) extra — at most 100 keys (values capped at 100); O(n) in general
Mistake : First used a set (only knows "seen", not "how many"); then used counter instead of num as the dict key.
"""

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        freq_map = {}
        counter = 0

        for num in nums:
            if num in freq_map:
                counter += freq_map[num]
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        return counter


if __name__ == "__main__":
    s = Solution()
    assert s.numIdenticalPairs([1, 2, 3, 1, 1, 3]) == 4
    assert s.numIdenticalPairs([1, 1, 1, 1]) == 6
    assert s.numIdenticalPairs([1, 2, 3]) == 0
    print("all tests passed")