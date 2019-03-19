//boj10950 A+B -3
import java.util.*;

class Main{
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0 ; i<n ; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.printf("%d",a+b);
            System.out.printf("\n");
        }
    }
}
