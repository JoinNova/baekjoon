//boj10950 A+B - 3
#include<stdio.h>
int main(void){
    int target, n, a, b;
    scanf("%d", &target)
    for(n=1;n<=target;n++){
        scanf("%d %d",&a ,&b);
        printf("%d\n",a+b);
    }
    return 0;
}
