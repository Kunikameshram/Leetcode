class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if word1 == word2 (or character as we will check character by character), operations = 0 shift both pointers i+1, j+1 
        # if word1 is empty,  then operations = len(word2) and viceversa
        # the last row and col of the dp would contain above 2 base case  
        # if pointer in word1 i ! = j pointer in word2, then below 3 options:
        # 1. insert, (i, j+1) since you inserted char at j but char at i is still incorrect, +1 opertaion
        # 2. delete, (i+1, j) since you deleted char at i but char at j is still not in word1, +1 operation
        # 3. Replace, (i+1, j+1) since you force the char at i to change to char at j, +1 operation

        dp = [[float("inf")] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range(len(word1)+1):
            dp[i][len(word2)] = len(word1) - i
        for j in range(len(word2)+1):
            dp[len(word1)][j] = len(word2) - j 
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i+1][j+1]) #min(insert, delete, replace)
        return dp[0][0]