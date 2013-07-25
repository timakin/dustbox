import java.util.*;

public class ShoutterDiv2{
    public int count(int[] s, int[] t){
        int ans=0;
        for (int i=0; i<s.length; i++) {
            for (int j=i+1; j<s.length; j++) {
                if ((s[i] <= s[j] && s[j] <= t[i]) || (s[j] <= s[i] && s[i] <= t[j])) {
                        ans++;
                }
            }
        }
        return ans;
    }
}