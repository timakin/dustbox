public class EelAndRabbit{
    public int getmax(int[] l, int[] t){
        int ans=0;
        int count=t.length;
        for (int i=0; i<count; i++) {
            for (int j=i; j<count; j++) {
                int curr = 0;
                int x = t[i], y = t[j];
                for (int k=0; k<count; k++) {
                    boolean containsX = (t[k] <= x && x <= t[k]+l[k]);
                    boolean containsY = (t[k] <= y && y <= t[k]+l[k]);
                    if (containsX || containsY) {
                        curr++;
                    }
                }
                ans = Math.max(ans, curr);
            }
        }
        return ans;
    }
}