class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        if len(s) > len(t):
            return False
        if not s:
            return True
        for t_pointer in range(len(t)):
            if s_pointer < len(s) and s[s_pointer] == t[t_pointer]:
                s_pointer += 1
        if s_pointer == len(s): 
            return True 
        else: 
            return False 