# Problem: 344. Reverse String
# Pattern: two pointers (opposite ends), in-place swap
# Idea:    left starts at 0, right at n-1; swap, move both inward; stop when left >= right
# Time:    O(n), n = len(s); n/2 swaps, constants dropped
# Space:   O(1) extra; only left, right and the swap, no matter how big s is
# Mistake: didn't know extra space at first; fixed-size variables = O(1)


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    sol = Solution()

    s = ["h", "e", "l", "l", "o"]          # odd length
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["a", "b", "c", "d"]               # even length
    sol.reverseString(s)
    assert s == ["d", "c", "b", "a"]

    s = ["x"]                              # edge case: single item
    sol.reverseString(s)
    assert s == ["x"]

    print("all tests passed")