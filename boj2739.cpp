//boj2739 구구단
#include<stdio.h>
int main(void) {
    int dan,n;
    scanf("%d",&dan);
    for(n=1;n<10;n++){
        printf("%d * %d = %d\n",dan,n,dan*n);
    }
    return 0;
}
