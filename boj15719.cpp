//boj15719 중복된숫자
#include<stdio.h>
int main(void){
    int n,i,arg,result;
    long long sum=0;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&arg);
        sum+=arg;
    }
    result=sum-(long long)n*(n-1)/2;
    printf("%d",result);
    return 0;
}



//by BaaaaaaaaaaarkingDog
#include <iostream>
using namespace std;
typedef long long ll;
int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	ll N;
	cin >> N;
	int t;
	ll s = 0;
	for (int i = 0; i < N; i++) {
		cin >> t;
		s += t;
	}
	cout << (s - N * (N - 1) / 2);
}
