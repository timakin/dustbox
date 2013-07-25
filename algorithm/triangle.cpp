//#include <cstdio>;//

//int n, a[MAX_N];//

//void solve() {
//    int ans = 0;//

//    for (int i = 0; i < n; ++i) {
//        for (int j = i+1; j < n; ++j) {
//            for (int k = j+1; k < n; ++k) {
//                int len = a[i]+a[j]+a[k];
//                int max = max(a[i],max(a[j],a[k]);
//                int rest = len-max;
//                if (rest>max)
//                {
//                    ans=max(ans,len);
//                }
//            }
//        }
//    }
//}


#include <cstdio>;

int n,a[MAX_N];

void solve() {
    int ans = 0;
    for (int i=0; i<n; ++i){
        for (int j = 0; j < n; ++j){
           for (int k = 0; k < n; ++k){
               int len=a[i]+a[j]+a[k];
               int ma =max(a[i], max(a[j], a[k]));
               int rest=len-ma;
               if (ma<rest){
                   ans=max(ans,len);
               }
           }
        }
    }
}