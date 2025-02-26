class Solution(object):
    def majorityElement(self, arr):
        num1=len(arr)/2
        arr.sort()
        count=1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                count=count+1
                if count>num1:
                    return arr[i]
    
