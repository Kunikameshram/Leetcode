class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursive not efficient
        res = 0
        def dfs(i, total):
            if i == len(nums):
                # Check if the current total equals the target
                return 1 if total == target else 0
            
            res = dfs(i+1, total+nums[i]) + dfs(i+1, total-nums[i])
            return res
        return dfs(0, 0)

        # recursion with DP
        dp = {} #(index, total) - number of ways
        
        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i]))
            return dp[(i, total)]
        return backtrack(0,0)