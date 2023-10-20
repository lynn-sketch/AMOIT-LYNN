#include <stdio.h>
#include <stdlib.h>



int main() {
	//SOLOMONS BUSINESS
	
	int Solomon[3][2] = {{500000,55000},{900000,200000},{650000,160000}};
	int count = 0;
	int saving;
	
	
	//SAVINGS FOR DAIRY BUSINESS
	 printf("SOLOMONS SAVING FOR DAIRY BUSINESS\n\n");
	 int savings = Solomon[0][0] - Solomon[0][1];
	 printf("%d is the savings for dairy busines\n\n");
	 count+=savings;
	 
	 //SAVINGS FOR PRODUCE BUSINESS
	  printf("SOLOMONS SAVING FOR PRODUCE BUSINESS\n\n");
	 savings = Solomon[1][0] - Solomon[1][1];
	 printf("%d is the savings for produce business\n\n",savings);
	 count+=savings;
	 
	 //SAVINGS FOR MOBILE MONEY BUSINESS
	 printf("SOLOMONS SAVING FOR MOBILE MONEY BUSINESS\n\n");
	 savings = Solomon[2][0] - Solomon[2][1];
	 printf("%d is the savings for mobile money business\n\n",savings);
	 count+=savings;
	 
	printf("Total savings\n\n");
	printf("%d is the sum of Solomons savings",count);
return 0;
}


