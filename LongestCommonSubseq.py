class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # Initialize dp matrix with (len(text2)+1) cols and (len(text1)+1) rows
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        # for row in dp:
        #     print(" ".join(str(elem) for elem in row))

        # Fill the DP table from the bottom-right corner to the top-left
        for i in range(len(text1)-1, -1, -1): # Traverse text1 in reverse order
            for j in range(len(text2)-1, -1, -1): # Traverse text2 in reverse order

                if text1[i] == text2[j]:  # If characters match
                    dp[i][j] = 1+ dp[i+1][j+1] #Diagonal value
                else: 
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) # Otherwise, take the maximum from right or below
        return dp[0][0] # Return the result from dp[0][0], which contains the length of LCS
