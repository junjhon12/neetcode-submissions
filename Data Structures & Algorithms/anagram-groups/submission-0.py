class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs is None: return [[""]]
        if len(strs) < 1: return [["x"]]
        
        from collections import defaultdict

        grouped = defaultdict(list)

        for word in strs:
            grouped["".join(sorted(word))].append(word)
        
        return list(grouped.values())