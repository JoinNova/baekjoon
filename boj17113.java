//컴파일에러용
import java.util.Scanner;

public class room {
 public static void main(String [] args)
 { Scanner scanner = new Scanner(System.in);
  
  int num = scanner.nextInt();
  int n=1;
  int i=10;
  int share , result;
  result = 1;
  int check=1;
  int setnumber;
  for(i=10 ; num-i>=0;i=i*10)
  {
   n++;
  }

  int arr[] = new int[n];
  for(int j = 0 ; j<n;j++)
  {
   share = num/10;
   arr[j] = num%10;
   num = share;
  }
  for(int j = 0 ; j < n ; j++)
  { 
   if(n==1)
  {
   result  = 1;
  }
   for(int a = j+1 ; a<n ; a++)
   {
    if((arr[j]==6 && arr[a]==9) ||(arr[j]==9 && arr[a]==6) || (arr[j]==6 && arr[a]==6) || (arr[j]==9 && arr[a]==9) )
    {
     check +=1;
     break;
    }
   else if(arr[j]==arr[a])
    { 
 
     result++;
     break;
     
    }
   }
  
  
  }
  check = check / 2 ;
  if(check > result )
   setnumber = check ;
  else
   setnumber = result ;
  System.out.println(setnumber);
 }
}
