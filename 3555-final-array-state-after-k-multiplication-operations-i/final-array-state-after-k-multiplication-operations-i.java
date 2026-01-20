class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
    // System.out.print(min);
    
    boolean flag=false;
    for(int x=0;x<k;x++){
        int min=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<nums[min]){
                min=i;
                flag=true;   
            }
    }
    nums[min]=nums[min]*multiplier;
    // System.out.print(min);

    }
    return nums;
    }
}