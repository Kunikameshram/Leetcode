class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings = [''.join(sorted(s)) for s in strs]
        print(sorted_strings)

        string_indices = {}


        for i, s in enumerate(sorted_strings):
            if s in string_indices:
                string_indices[s].append(i)  
            else:
                string_indices[s] = [i] 

        print(string_indices)
        res = []

        for key, value in string_indices.items():
            res.append([strs[v] for v in value])

        return res