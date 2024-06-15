import math 


welcome ="""Benvenuti al progeamma per calcolare l'area e perimetri di diverse figure geometriche;

-Di seguito un elenco delle varie funzioni disponivili:

-Per calcolare il perimetro e area di un quadrato premere A; 
-Per calcolare circonferenza e area di un cerchio premere B;   
-Per calcolare il perimetro e area  un rettangolo premere C;
-Per uscire dal programma o continuare ad utilizarlo Y/N;
"""

while True:

    
    print (welcome)
                 
    action = input("inserisci il carattere corispondente al calcolo da efettuare\n" )
    
    if action == 'a' or action == 'A':
        print("\nHai scelto calcolare il perimetro e area di un quadrato\n")
        a = float(input("Digita un numero che corrisponderà a un lato del quadrato\n"))
        b = 4
        print(f"Il perimetro del quadratato è:  {a * b}\nL'area del quadrato è : {a * a}")
        
    if action == 'b' or action == 'B':
        print("\nHai scelto calcolare l'area e circonferenza appunto di cerchio\n")
        raggio = float(input("Inserisci il valore del raggio:\n"))
        diametro = 2*raggio
        circonferenza = 2*math.pi*raggio
        area = math.pi*raggio**2
        print(f"L'area del cerchio è : {area}\n La circonferenza del cerchio è: {circonferenza} " )
        
    if action == 'c' or action == 'C':
        print("\nHai scelto calcolare il perimetro e area di un rettangolo\n")
        a = float(input("Digita il primo numero\n"))
        b = float(input("Digita il secondo numero\n"))
        
        print(f"Il perimetro del rettangolo è:  {a*2 + b*2}\nL'area del rettangolo è : {a*2 * b*2}")        
        
    new_action = input("\nDesideri continuare ad utilizare l'Aplicazioine: Y/N  ")
    if new_action == 'Y' or new_action =='y':
        print("Torniamo al menu principale\n")
        continue
    else:
        print("\nA PRESTO\n")
        break

        
    
                 
                 
             
            

         



  
  
  
  
  
  
  
  
  

