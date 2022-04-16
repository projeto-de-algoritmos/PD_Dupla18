import java.util.Arrays;

class Solution {
Boolean[] previous;
int[] nums;

    public static void main(String[] args) {
		// TODO Auto-generated method stub
        int[] g = {2,3,1,1,4}; //Caso deseje, modifique aqui o array com a distância dos pulos.
        var classCanJump = new Solution();

        System.out.println("Resposta:\n");
        System.out.println(classCanJump.canJump(g));
	}
    
    public boolean canJump(int[] nums) {

        int n = nums.length;
        this.nums = nums;
        this.previous = new Boolean[n];

        return dfs(0);

    }

    private boolean dfs(int index){
        
        if(nums.length - 1 <= index)
            return true;
        
        if(previous[index] != null) 
            return previous[index];
        
        int reachable = nums[index];
        
        for(int i = 1; i <= reachable; i++){
            boolean res = dfs(index + i);
            if(res){
                previous[index] = true;
                return previous[index];
            }
            
        }
        
        return previous[index] = false;
    }
};