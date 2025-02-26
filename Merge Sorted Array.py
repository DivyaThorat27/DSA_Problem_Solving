class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i] 

        
        for i in range(n+m):
            for j in range(i+1,n+m):
                if nums1[i]>nums1[j]:
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp                
            
        return nums1



        
        
