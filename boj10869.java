//boj10869 사칙연산
import java.util.*;

class Main{
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.printf("%d\n%d\n%d\n%d\n%d",a+b,a-b,a*b,a/b,a%b);
    }
}
