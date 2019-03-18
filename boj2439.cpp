//boj2439 별찍기2
#include<stdio.h>
int main(void){
    int i,j,target;
    scanf("%d",&target);
    for(i=1;i<=target;i++){
        for(j=target-i;j>=1;j--){
            printf(" ");
        }
        for(j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
     }
    return 0;
}
