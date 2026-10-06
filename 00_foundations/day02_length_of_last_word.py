# Problem: 58. Length of Last Word
# Pattern: scan from the end (two phases: skip, then count)
# Idea:    start i at the last index; phase 1 skips trailing spaces;
#          phase 2 counts letters until a space or the front of the string
# Time:    O(n), n = len(s); i only moves left, at most n steps across both loops
# Space:   O(1) extra; only i and count
# Built-in alternative: len(s.split()[-1]) -> O(n) time, O(n) space (builds a list of words)
#          s.split(" ")[-1] is WRONG with trailing spaces (gives '')
# Mistake: compared i (an index) with " " instead of s[i]; moved i the wrong way (+1);
#          phase 1 loop never stopped on a letter -> infinite loop


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0

        # Phase 1: skip trailing spaces
        while i >= 0:
            if s[i] == " ":
                i -= 1
            else:
                break

        # Phase 2: count letters of the last word
        while i >= 0:
            if s[i] == " ":
                break
            count += 1
            i -= 1

        return count


if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLastWord("Hello World") == 5
    assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert sol.lengthOfLastWord("luffy is still joyboy") == 6
    assert sol.lengthOfLastWord("a") == 1          # edge: phase 2 runs to i = -1
    assert sol.lengthOfLastWord("hello") == 5      # edge: no spaces at all
    print("all tests passed")