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

//ansは同時に取れるうなぎの最大の数
//x,yを作り、２回取れるタイミングのうちどちらかが、あるうなぎの
//範囲内に収まる場合はカウント
//i,jはタイミング、kはうなぎの位置を表している。
//2つのタイミングがあるとき、count匹のうなぎがどれだけ
//そのタイミングに重なって捕獲されるんですか？と聞いている。