
#include <stdio.h>

void stampaMenu(){
    
    printf("\nA:   Home run.(palla fuori campo da fondo)");
    printf("\nB:   Foul (palla fuori campo laterale)");
    printf("\nE:   esci");
    printf("\n AMERCAN BASEBALL\n ");
}

int main(){
    char scegli = '\0';
    while (scegli != 'E')
    {
        stampaMenu();
        printf("\n  Scegli una domanda: ");
        scanf(" %c", &scegli);
        switch (scegli)
        {
        case 'A':
        case 'a':
            printf("\n  Ottiene un punto immediato");
            break;
        case 'B':
        case 'b':
            printf("\n  Fallo( 4 volte consecutive sei fuori gioco");
            break;
        case 'e':
            scegli = 'E';
           
        default:
            printf("\nArrivederci");
            break;
        }
    }
    
    return 0;
}
