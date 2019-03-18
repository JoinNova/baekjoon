//boj2438 별찍기1
#include<stdio.h>
int main(void){
    int i,j,target;
    scanf("%d",&target);
    for(i=1;i<=target;i++){
        for(j=1;j<=i;j++){
            printf("*");
        }
        printf("\n");
     }
    return 0;
}
