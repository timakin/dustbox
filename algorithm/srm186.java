public class GolfScore{
    public int tally(int[] parValues, String[] scoreSheet){
        int ans=0;
        for (i=0; i<scoreSheet.length; i++) {
            switch(scoreSheet[i])
            case "triple bogey":
                ans += parValues[i]+3;
                break;
            case "double bogey":
                ans += parValues[i]+2;
                break;
            case "bogey":
                ans += parValues[i]+1;
                break;
            case "par":
                ans += parValues[i];
                break;
            case "birdle":
                ans += parValues[i]-1;
                break;
            case "eagle":
                ans += parValues[i]-2;
                break;
            case "albatross":
                ans += parValues[i]-3;
                break;
            case "hole in one":
                ans += 1;
                break;
        }
        return ans;
    }
}

import java.util.*;
public class GolfScore{
    public int tally(int[] parValues, String[] scoreSheet){
        int ans = 0;
        String scoreList[] = ["triple bogey","double bogey","bogey","par","birdie","eagle","albatross"];
        Int pointList[] = [3,2,1,0,-1,-2,-3];
        for (int i=0; i<parValues.length; i++) {
            if (scoreSheet[i]=="hole in one") {
                ans++;
            } else {
                for (int j=0; j<scoreSheet.length; ) {
                    
                }
                if (scoreSheet[i]) {
                    
                }
            }
        }


    }
}