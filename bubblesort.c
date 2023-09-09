#if 0
gcc -o $0.out $0 && ./$0.out
rm ./$0.out > /dev/null
exit
#endif

#include<stdio.h>
#include<stdlib.h>
#include<string.h>


int main(){
  int p[10]={1,2,35,76,2,3,4,5,0,12}; 
  int length=10;
  int ans[10];
  int i,j=0;

for (i=length-2;i>=0;i--){
  for (j=0;j<=i;j++){
    if((p[j])>(p[j+1]))
    {
      p[j]=p[j]-p[j+1];
      p[j+1]=p[j+1]+p[j];
      p[j]=p[j+1]-p[j];

    }
  }
}
for (i=0;i<length;i++){ 
  printf(" %d ,",p[i]);
}
  
}
