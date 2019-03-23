//boj17013 Flipper
#include<stdio.h>

int main(void){
        int arr[4]={1,2,3,4};
        int cnt[85]={};
        char HV[1000001];
        int i,temp;
        scanf("%s",HV+1);
        while(HV[++i]!='\0'){
                cnt[HV[i]]++;
        }
        if(cnt['H']%2){
            temp=arr[0];
            arr[0]=arr[2];
            arr[2]=temp;
            temp=arr[1];
            arr[1]=arr[3];
            arr[3]=temp;
        }
        if(cnt['V']%2){
            temp=arr[0];
            arr[0]=arr[1];
            arr[1]=temp;
            temp=arr[2];
            arr[2]=arr[3];
            arr[3]=temp;
        }
        printf("%d %d\n%d %d",arr[0],arr[1],arr[2],arr[3]);
        return 0;
}


//boj17013 Flipper
#include<stdio.h>
#include<iostream>
using namespace std;

int main(void){
        int arr[2][2]={1,2,3,4};
        int cnt[256]={};
        char HV[1010001];
        int i;
        scanf("%s",HV+1);
        while(HV[++i]!='\0'){
                cnt[HV[i]]++;
        }
        if(cnt['H']%2)swap(arr[0],arr[1]);
        if(cnt['V']%2)swap(arr[0][0],arr[0][1]),swap(arr[1][0],arr[1][1]);
        printf("%d %d\n%d %d",arr[0][0],arr[0][1],arr[1][0],arr[1][1]);
        return 0;
}

//by kyo20111
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
char s[1010101];
int cnt[256],i,ans[3][3] = {{0,0,0},{0,1,2},{0,3,4}};
int main(){
    scanf("%s",s+1);
    while(s[++i] != '\0') cnt[s[i]]++;

    if(cnt['H'] % 2) swap(ans[1][1],ans[2][1]),swap(ans[1][2],ans[2][2]);
    if(cnt['V'] % 2) swap(ans[1][1],ans[1][2]),swap(ans[2][1],ans[2][2]);

    printf("%d %d\n%d %d",ans[1][1],ans[1][2],ans[2][1],ans[2][2]);
}
