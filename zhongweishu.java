import java.util.Scanner;

public class yulie_zhongweishu {

	public static void main(String[] args) {

		Scanner sc = new Scanner (System.in);
		int a = sc.nextInt();
		int s1[] = new int[a+1];
		int s2[] = new int[a+1];
		
		for (int i=0;i<a;i++){
			s1[i]=sc.nextInt();
		}
		
		for (int i=0;i<a;i++){
			s2[i]=sc.nextInt();
		}
		search(s1,s2,a);}
	public static void search(int a[],int b[],int n) {
		int l1 = 0,l2 = 0;
		int r1 = n-1,r2 = n-1;
		int mid1,mid2;
		while (l1 <r1&&l2 <r2){
			mid1 = (l1 + r1) / 2;
			mid2 = (l2 + r2) / 2;
			if ( a[mid1] == b[mid2]){
				System.out.print(a[mid1]);
			}
			else if (a[mid1] < b[mid2]){
				
				if((l1 + r1) % 2 == 0){
					l1 = mid1;
					r2 = mid2;
				}
				else{
					l1 = mid1 + 1;
					r2 = mid2;
				}
			}
			else{
				
				if((l1 + r1) % 2 == 0){
					
					r1 = mid1;
					l2 = mid2;
				}
				else{
					r1 = mid1;
					l2 = mid2 + 1;
				}
			} 	
		}
		if (a[l1] < b[l2]){
			System.out.print(a[l1]);
		}
		else{
			System.out.print(b[l2]);
		}
	}
	}



