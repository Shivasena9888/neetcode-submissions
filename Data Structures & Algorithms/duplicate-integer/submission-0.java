class Solution {
    public boolean hasDuplicate(int[] nums) {

      HashSet<Integer> map = new HashSet<>();

      for(int i =0; i<nums.length; i++){
        int num = nums[i];
        if(map.contains(num)){
            return true;
        }
        map.add(num);
      }
      return false;
    }
}