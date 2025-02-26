class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(target>nums[i] && target>nums[j]){
                    int sum1=nums[i]+nums[j];
                    if(sum1==target){
                        return new int[]{i,j};
                    }
                }
            }
        }
        return new int[]{};
        
    }
}
