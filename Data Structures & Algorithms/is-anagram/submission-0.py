class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for v in s:
            map1[v] = map1.get(v, 0) + 1
        for v in t:
            map2[v] = map2.get(v, 0) + 1
        if map1 == map2:
            return True
        else:
            return False
        