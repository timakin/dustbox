class WallGameDiv2 {
public:

    void putMax( int& target, int value ){
        target = max( target, value );
    }

    int play(vector <string> costs){
        //縦の長さheight、配列contsに値として入っているものの数
        //横の長さwidth、配列costsの0番目に入っている数字の数
        int h = costs.size();
        int w = costs[0].length();

        // dp初期化
        int dp[55][55];
        memset( dp, -1, sizeof(dp) );
        dp[0][0] = 0;

        // dp更新
        for( int y = 0; y < h - 1; y++ ){
            for( int x = 0; x < w; x++ ){
            if( dp[y][x] == -1 ) continue;

                // そのまま下へ
                if( costs[y+1][x] != 'x' ){
                    int downCost = costs[y+1][x] - '0';
                    putMax( dp[y+1][x], dp[y][x] + downCost );
                }

                // 右に動いて下へ
                int rowCost = 0;
                for( int nx = x + 1; nx < w && costs[y][nx] != 'x'; nx++ ){
                    rowCost += costs[y][nx] - '0';
                    if( costs[y+1][nx] != 'x' ){
                        int downCost = costs[y+1][nx] - '0';
                        putMax( dp[y+1][nx], dp[y][x] + rowCost + downCost );
                    }
                }

                // 左に動いて下へ
                rowCost = 0;
                for( int nx = x - 1; nx >= 0 && costs[y][nx] != 'x'; nx-- ){
                    rowCost += costs[y][nx] - '0';
                    if( costs[y+1][nx] != 'x' ){
                        int downCost = costs[y+1][nx] - '0';
                        putMax( dp[y+1][nx], dp[y][x] + rowCost + downCost );
                    }
                }
            }
        }

        // 集計
        int res = 0;
        for( int x = 0; x < w; x++ ){
            res = max( res, dp[h-1][x] );
        }
                        
        return res;
    }    
};