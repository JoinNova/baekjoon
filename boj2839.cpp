//boj2839  설탕배달
#include<stdio.h>

int main(void){
    int n,i,result;
    scanf("%d",&n);
    if(n==4 || n==7){
        result=-1;
        printf("%d",result);
    }else{
        for(i=0;i<5;i++){
            if((n-(3*i))%5==0){
                result=i+(n-(3*i))/5;
                printf("%d",result);
                break;
            }
        }
    }
    return 0;
}
