#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h> 
#include <unistd.h> 

#include "myexample.h"

void helloworld()
{
    printf("C HelloWorld");
}

//return random value in range of 0-50
int pyfork()
{   
    //you can fork processes in C too, 
    //with all the disadvantages that has 
    //in this case this is safe, because it will fork the python process
    //which will to it's thing, adding and printing and exit normally
    fork();
}

//add two number and return value
int addNum(int a, int b)
{
    int nAdd = a + b;
    return nAdd;
}
