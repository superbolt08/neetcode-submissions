class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = sorted(strs, key=len)
        groups = []
        visited = set()

        for i in range(len(sorted_words)):
            if i in visited:
                continue
            group = [sorted_words[i]]
            for j in range(i + 1, len(sorted_words)):
                if len(sorted_words[i]) != len(sorted_words[j]):
                    break  # no need to check further, lengths differ
                if sorted(sorted_words[i]) == sorted(sorted_words[j]):
                    group.append(sorted_words[j])
                    visited.add(j)
            groups.append(group)

        return groups