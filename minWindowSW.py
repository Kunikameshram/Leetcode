class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "": return ""

        window, t_count = {}, {}
        l, res, resLen = 0, [-1, -1], float("infinity")

        # t_count = Counter(t)
        for char in t:
            t_count[char] = 1 + t_count.get(char, 0)
           
        have, need = 0, len(t_count)

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in t_count and window[c] == t_count[c]:
                have +=1 

            while have == need:

                # update result
                if (r-l+1) < resLen:
                    resLen = (r-l+1)
                    res = [l, r]
                # shrink the window to get minimum substring
                window[s[l]] -= 1
                # stop shrinking if any of the characters in t is not present in window anymore
                if s[l] in t_count and window[s[l]] <  t_count[s[l]]:
                    have -= 1
                l +=1
        l, r = res #extracting the left and right pointers from the result

        return s[l:r+1] if resLen != float("infinity") else ""