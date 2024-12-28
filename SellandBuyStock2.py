class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_prof = 0
        max_prof = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                cur_prof = cur_prof + (prices[i] - prices[i-1])
                
            elif prices[i-1] > prices[i]:
                max_prof = max_prof + cur_prof
                cur_prof = 0
        max_prof = max_prof + cur_prof    
        return max_prof