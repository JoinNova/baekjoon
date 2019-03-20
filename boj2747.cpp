//boj2747 피보나치수
#include<stdio.h>

int main(void){
    long long a,b,temp;
    int idx,target;
    idx=1;
    a=1;
    b=1;
    scanf("%d",&target);
    while(1){
        if(idx==target)break;
        temp=a;
        a=b;
        b=b+temp;
        idx+=1;
    }
    printf("%lld",a);
    return 0;
}
