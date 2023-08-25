#if 0
gcc -o $0.out $0 && ./$0.out $@ 
rm -f $0.out
exit
#endif

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<stdbool.h>

// Might be the foolish way to do so , But for sake of learning , it's done as it is 
typedef struct{
    int top;
    char* array;
}stack ;
stack createStack(int length){
    stack s;
    s.array=malloc(sizeof(char)*length);
    s.top=0;
    return s; 
}
bool isgreaterthanzero(int top){
    return top>0;
}
bool  isValid(char * argv){
    int length=strlen(argv);
    stack too=createStack(length);
    if (length<=1) return false;
    for (int i=0;i<length;i++){  
        if((isgreaterthanzero(too.top))&& ((argv[i]==')' && too.array[too.top-1]=='(' ) ||        (argv[i]=='}' && too.array[too.top-1]=='{') ||(argv[i]==']' && too.array[too.top-1]=='['))){
        too.top--;
        }          
        else if((argv[i]=='(') ||(argv[i]=='{') ||(argv[i]=='[') ){
            too.array[too.top++]=argv[i];

        }
        else{
            return false;
        }
}
 return too.top==0; 
}

int main(int argc,char* argv[]){
    printf("The final answer is TRUE OR FALSe i.e 1 or 0    ::  %d",isValid(argv[1]));
    return 0;
}