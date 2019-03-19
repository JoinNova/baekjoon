//boj11718 그대로 출력하기
import java.util.*;

public class Main {
    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        while (input.hasNext())
            System.out.println(input.nextLine());
    }
}



//boj11718 그대로 출력하기
//import java.io.BufferedReader;
//import java.io.BufferedWriter;
//import java.io.InputStreamReader;
//import java.io.OutputStreamWriter;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        while (true) {
            String str = br.readLine();
            
            if (str != null) {
                bw.write(str);
                bw.newLine();
            } else {
                break;
            }
        }
        
        br.close();
        bw.flush();
        bw.close();
    }

}
