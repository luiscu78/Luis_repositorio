#include <stdio.h>

int main(){
    int base, altezza;
    float area;

	printf("Inserisci la base del triangolo: ");
	scanf("%d", &base);
    printf("Inserisci l'altezza del triangolo: ");
	scanf("%d", &altezza);

    area = (base*altezza)/2.0;

	printf("L'area del triangolo vale: %.2f", area);

	return 0;
}