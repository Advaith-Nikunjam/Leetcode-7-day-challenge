class Solution(object):
    def findMaxAverage(self, nums, k):
        # max_sum = float('-inf')
        # for i in range(len(nums) - k + 1):
        #     current_sum = 0 
        #     for j in range(i, i + k):
        #         current_sum += nums[j] 
        #     if current_sum > max_sum:
        #         max_sum = current_sum
        # average = max_sum / k 
        # return average
        
        
        current_sum = sum(nums[:k])
        max_sum = current_sum
        for i in range(k,len(nums)):
            current_sum+=nums[i] - nums[i-k]
            if current_sum > max_sum:
                max_sum = current_sum
        average = max_sum/k
        return average