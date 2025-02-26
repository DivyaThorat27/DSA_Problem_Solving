class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i!=j:
                    if target>=nums[i] and target>=nums[j]:
                        sum_numbers=nums[i]+nums[j]
                        if sum_numbers==target:
                            return i,j

        
