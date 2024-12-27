class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLen = float("infinity")
        curSum = 0
        for r in range(0, len(nums)):
            curSum = curSum + nums[r]
            while curSum >= target:
                if (r-l+1) < minLen:
                    minLen = (r-l+1)
                curSum -= nums[l]
                l += 1
        return minLen if minLen != float("infinity") else 0