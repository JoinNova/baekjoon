//boj2739 구구단
import java.util.*;

class Main{
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for( int i = 1 ; i <= 9 ; i++ ){
            System.out.println(n+" * "+i+" = "+n*i);
        }
    }
}
