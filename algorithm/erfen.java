import java.util.Scanner;

public class erfen {

	public static void main(String[] args) {

		Scanner sc = new Scanner (System.in);
		int a = sc.nextInt();
		int search = sc.nextInt();
		int src[] = new int[a];
		for (int i=0;i<a;i++){
			src[i]=sc.nextInt();
		}
		
		binarySearch(src, search);
	}

   public static void binarySearch(int[] srcArray, int des){ 
	
		int low = 0; 
		int high = srcArray.length-1; 
		
		while(low <= high ) {  
			int middle = (low + high)/2; 
			if(des == srcArray[middle]) { 
				System.out.print(middle + " " + middle);
				System.exit(0);
			}
			else if(des <srcArray[middle]) { 
			    high = middle - 1; 
			}
			else { 
			    low = middle + 1; 
			}
		}
		
		
		int high4 = high+1;
		if(low==high){
			System.out.print(low + " " +  high4);			
			}
		else{
			System.out.print(low-1 + " " + low);
		}


   }	
	}

