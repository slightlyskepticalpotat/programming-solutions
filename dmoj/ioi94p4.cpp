#include<stdio.h>
#include<string.h>
int a[15],d[15],t[15], ind=1;
int main()
{
    for(int i=1; i<=9; ++i)
        scanf("%d", & a[i]);
    for (int i = 1; i <= 9; i++) {
        if (a[i] == 0) {
            a[i] = 12;
        } else if (a[i] == 1) {
            a[i] = 3;
        } else if (a[i] == 2) {
            a[i] = 6;
        } else {
            a[i] = 9;
        }
    }
    for(d[1]=0; d[1]<=3; ++d[1])
        for(d[2]=0; d[2]<=3; ++d[2])
            for(d[3]=0; d[3]<=3; ++d[3])
                for(d[4]=0; d[4]<=3; ++d[4])
                    for(d[5] = 0; d[5] <= 3; ++ d[5])
                        for(d[6] = 0; d[6] <= 3; ++ d[6])
                            for(d[7] = 0; d[7] <= 3; ++ d[7])
                                for(d[8] = 0; d[8] <= 3; ++ d[8])
                                    for(d[9] = 0; d[9] <= 3; ++ d[9]){
                                        if((a[1] + 3*(d[1]+d[2]+d[4]))% 12 != 0) continue;
                                        if((a[2] + 3*(d[1]+d[2]+d[3]+d[5]))% 12 != 0) continue;
                                        if((a[3] + 3*(d[2]+d[3]+d[6]))% 12 != 0) continue;
                                        if((a[4] + 3*(d[1]+d[4]+d[5]+d[7]))% 12 != 0) continue;
                                        if((a[5] + 3*(d[1]+d[3]+d[5]+d[7]+d[9]))% 12 != 0) continue;
                                        if((a[6] + 3*(d[3]+d[6]+d[5]+d[9]))% 12 != 0) continue;
                                        if((a[7] + 3*(d[4]+d[7]+d[8]))% 12 != 0) continue;
                                        if((a[8] + 3*(d[5]+d[7]+d[8]+d[9]))% 12 != 0) continue;
                                        if((a[9] + 3*(d[6]+d[8]+d[9]))% 12 != 0) continue;
                                        for(int i = 1; i <= 9; ++ i){
                                            if(d[i]){
                                                int tmp = d[i];
                                                while(tmp>0){
                                                    t[ind++] = i;
                                                    -- tmp;
                                                }
                                            }
                                        }
                                        for(int i=1; i<ind; ++i){
                                            if(i < ind-1) printf("%d ", t[i]);
                                            else printf("%d\n",t[i]);
                                        }
                                    }
}