#include <stdio.h>
#include <math.h>

int main(){
	int raggio;
    float circ, area;

	printf("Inserisci il valore del raggio: ");
	scanf("%d", &raggio);

    circ = 2*M_PI*raggio;
    area = M_PI*pow(raggio, 2);

	printf("La circonferenza del cerchio vale: %.2f\n", circ);
	printf("L'area del cerchio vale: %.2f\n", area);

	return 0;
}
