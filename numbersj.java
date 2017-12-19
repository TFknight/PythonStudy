import java.util.Scanner;

public class numbersj {
	public static int[][] m ;
	public static void main(String[] args) {
	Scanner sc = new Scanner(System.in);
	int n = sc.nextInt();
	m = new int[n][n];
	
	for(int i = 0;i<n;i++){
		for(int j = 0;j<=i;j++){
			m[i][j] = sc.nextInt();
		}		
	}
	
	for(int i = n-1;i>0;i--){
		for(int j = 0;j<i;j++){
			m[i-1][j] += Math.max(m[i][j], m[i][j+1]);
			
		}
	}
	System.out.print(m[0][0]);
	
	
}
}