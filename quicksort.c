#include<stdio.h>
#define INPUT_SIZE 3000
void quicksort(int number[INPUT_SIZE],int first,int last){
    int i, j, pivot, temp;

    if(first<last){
        pivot=first;
        i=first;
        j=last;

    while(i<j){
        while(number[i]<=number[pivot]&&i<last)
            i++;
        while(number[j]>number[pivot])
             j--;
        if(i<j){
             temp=number[i];
            number[i]=number[j];
            number[j]=temp;
         }
    }

    temp=number[pivot];
    number[pivot]=number[j];
    number[j]=temp;
    quicksort(number,first,j-1);
    quicksort(number,j+1,last);

    }
}

int main(){

    int inputNumbers[INPUT_SIZE];
    
    for (int i = 0; i<INPUT_SIZE; i++){
        inputNumbers[i] = rand();
    }
    
    quicksort(inputNumbers,0,INPUT_SIZE - 1);
    return 0;
}
