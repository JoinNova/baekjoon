//boj11718 그대로출력하기
#include <stdio.h>
int main(void) {
	char str[101];

	while (scanf("%[^\n]%\n", str) != EOF) {
		printf("%s\n", str);
	}

	return 0;
}
