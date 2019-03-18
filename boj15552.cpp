//boj15552 빠른 A+B
#include<stdio.h>
int main(void){
    int a,b;
    unsigned int target,n;
    scanf("%d",&target);
    for(n=1;n<=target;n++){
        scanf("%d %d",&a,&b);
        printf("%d",a+b);
        if(n==target)break;
        printf("\n");
    }
    return 0;
}
