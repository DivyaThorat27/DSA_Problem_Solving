class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for(int i=0;i<n;i++){
            nums1[m+i]=nums2[i];
        }
        for(int i=0; i<n+m; i++){
            for(int j=i+1; j<n+m; j++){
                if(nums1[i]>nums1[j]){
                    int temp=nums1[j];
                    nums1[j]=nums1[i];
                    nums1[i]=temp;
                }
            }
        }
       
    }
}
