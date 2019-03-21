//boj2581 소수
#include<stdio.h>
#include<math.h>

int main(void){
    int m,n,i,j,min,hap,chk;
    hap=0;
    min=0;
    scanf("%d",&m);
    scanf("%d",&n);

    for(i=m;i<=n;i++){
        chk=0;
        for(j=2;j<=sqrt(i);j++){
                if(i%j==0){
                        chk=1;
                        break;
                }
        }
        if(chk==0){
                if(hap==0 && i!=1)min=i;
                if(i!=1)hap+=i;
        }
    }
    if(hap==0){
            hap=-1;
            printf("%d",hap);
     }else{
            printf("%d\n%d",hap,min);
    }
    return 0;
}
