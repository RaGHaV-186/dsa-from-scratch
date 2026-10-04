"""
Problem: 1672. Richest Customer Wealth (Easy)
Pattern: 2-D array traversal, running max
Idea:    Sum each customer's row; keep only the biggest sum seen so far.
Time:    O(m·n)
Space:   O(1) extra
Mistake: First plan stored all m sums in an array (O(m) extra) before taking max.
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0
        for account in accounts:
            current = sum(account)
            maximum = max(current, maximum)

        return maximum


# ---------- tests ----------
if __name__ == "__main__":
    s = Solution()

    assert s.maximumWealth([[1, 2, 3], [3, 2, 1]]) == 6
    assert s.maximumWealth([[1, 5], [7, 3], [3, 5]]) == 10
    assert s.maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]) == 17
    assert s.maximumWealth([[4]]) == 4                  # edge: 1 customer, 1 bank
    assert s.maximumWealth([[1, 1], [5, 5], [2, 2]]) == 10  # edge: richest in the middle

    print("All tests passed")