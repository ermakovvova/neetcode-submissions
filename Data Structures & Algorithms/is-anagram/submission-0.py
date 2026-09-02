class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        for char in s:
            c[char] = c.get(char, 0) + 1
        for char in t:
            c[char] = c.get(char, 0) - 1

        return all([count == 0 for count in c.values()])

        