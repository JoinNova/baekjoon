//boj15719 중복된숫자
/*
import java.io.*;
import java.util.*;

class Main{
    public static void main(String arg[]){
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        String line = br.readline();
        int split = line.indexOf(" ");
        for( int i=0 ; i<n ; i++ ){
            result += Integer.parseInt(line.substing(i,split));
        }
        bw.write(result);
        bw.flush();
        br.close();
        bw.close();
    }
}*/

public class Main{
    private static byte[] buffer = new byte[78888905];
    private static byte[] set = new byte[10000000];
    private static int next;
    private static byte b;
    
    public static void main(String arg[]) throws Exception{
        System.in.read(buffer,0,buffer.length);
        
        int N = nextInt();
        while(N-->0){
            int n = nextInt();
            
            if (set[n] == 1){
                System.out.print(n);
                break;
            }
            set[n] = 1;
        }
    }
    private static int nextInt(){
        int n = buffer[next++] - '0';
        while ((b=buffer[next++])>='0'){
            n = (n*10) + (b-'0');
        }
        return n;
    }
}
