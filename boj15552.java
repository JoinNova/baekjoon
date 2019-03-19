//boj15552 빠른 A+B
import java.io.*;
import java.util.*;

class Main{
    public static void main(String arg[])throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        
        for( int i=0 ; i<n ; i++ ){
            String line = br.readLine();
            int split = line.indexOf(" ");
            result = Integer.parseInt(line.substring(0,split)) + Integer.parseInt(line.substring(split+1,line.length()));
            bw.write(result+"\n");

        }
        bw.flush();
        br.close();
        bw.close();
    }
}
