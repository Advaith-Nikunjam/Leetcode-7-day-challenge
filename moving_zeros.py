class Solution(object):
    def moveZeroes(self, nums):
        zeros = []
        i = 0
        while i<len(nums):
            if nums[i] == 0:
                zeros.append(0)
                nums.pop(i)
            else:
                i = i+1
        nums.extend(zeros)
        return nums