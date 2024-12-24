class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n = len(nums)
        # sum1 = 0
        # for i in nums:
        #     sum1 += i
        # return n * (n + 1) // 2 - sum1

        # res = len(nums) 

        # for i in range(len(nums)):
        #     res += (i - nums[i])
        # return res

        # XOR
        res = 0
        for i in range(len(nums)+1):
            res = res ^ i
        for n in nums:
            res = res ^ n
        return res