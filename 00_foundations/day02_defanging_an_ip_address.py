# Problem: 1108. Defanging an IP Address
# Pattern: build a string with list + join
# Idea:    walk the address once; append "[.]" for a dot, else the char; join once at the end
# Time:    O(n), n = len(address); each char visited once, join copies once
# Space:   O(n) extra for the list + O(n) output (n <= 15 for a valid IPv4)
# Mistake: called "".join(parts) but the list was named res -> NameError


class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = []
        for ch in address:
            if ch == ".":
                res.append("[")
                res.append(ch)
                res.append("]")
            else:
                res.append(ch)

        res = "".join(res)
        return res


if __name__ == "__main__":
    sol = Solution()
    assert sol.defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
    assert sol.defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
    print("all tests passed")