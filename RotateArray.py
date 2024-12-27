class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        if len(nums) > k:
            j = 0
            for i in range(len(nums)-k, len(nums)):
                nums[j] = temp[i]
                j+=1
            
            for i in range(0, len(nums)-k):
                nums[j] = temp[i]
                j+=1
            
        elif len(nums) < k:
            j = 0
            for i in range(abs(2*len(nums)-k), len(nums)):
                nums[j] = temp[i]
                j+=1
            
            for i in range(0, abs(2*len(nums)-k)):
                nums[j] = temp[i]
                j+=1