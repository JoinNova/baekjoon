//boj2609최대공약수와 최소공배수
#include<stdio.h>
#include<math.h>

int gcd(int a,int b){
        if(a<b){
                return gcd(b,a);
        }else if(a>=b && fmod(a,b)==0){
                return b;
        }else{
                return gcd(b,fmod(a,b));
        }
}

int main(void){
        int x,y;
        scanf("%d %d",&x,&y);
        printf("%d\n%d",gcd(x,y),(x*y/gcd(x,y)));
        return 0;
}
