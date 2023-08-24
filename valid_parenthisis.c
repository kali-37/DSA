#if 0
gcc -o $0.out $0 && ./$0.out  $@
rm -f $0.out
exit
#endif

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct{
    char* top;
    char* array;
}stack ;

stack createStack(int length){
    stack s;
    s.top =malloc(sizeof(char*));
    s.array=malloc(sizeof(char*)*length);
    return s; 
}

int main(int argc,char* argv[]){

    if (argc!=2){
        printf("Sorry run programme with arguments  .\n\n");
    }
    else{
        stack  value=createStack(strlen(argv[1]));
    }

   return 0;
}


