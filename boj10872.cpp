//boj10872 팩토리얼
#include<stdio.h>

int main(void){
    long long fac;
    int target,idx;
    idx=1;
    fac=1;
    scanf("%d",&target);
    while(1){
        if(idx>=target)break;
        idx+=1;
        fac*=idx;
    }
    printf("%lld",fac);
    return 0;
}
