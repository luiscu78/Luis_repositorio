



#include <stdio.h>

int main () 
{
    
    int a,b,c;
    
    printf ("quanto misura il lato?\n");
    printf ("i valori sono espressi in cm\n");
    scanf ("%d" , &a);
    b= a*a;
    c= a+a+a+a;
    
    printf ("l' aera è %d\n",b);
    printf ("il perimetro è %d\n",c);
    return 0;
    
    
}