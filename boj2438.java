//boj2438 별 찍기 -1
import java.util.*;

class Main{
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.printf("*");
            }
            System.out.printf("\n");

        }
    }
}
