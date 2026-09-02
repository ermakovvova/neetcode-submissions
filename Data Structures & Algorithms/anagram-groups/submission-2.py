class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            hash = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                hash[idx] += 1
            groups[tuple(hash)].append(s)
        return list(groups.values())
        