class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        end = len(s) - 1
        while s[end] == " ":
            end -= 1
        start = end
        while start >= 0 and s[start] != " ":
                count += 1
                start-=1
        return count