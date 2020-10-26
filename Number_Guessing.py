import random
import math

Menor = int(input("Insira o menor limite : ")) 
 
Maior = int(input("Insira o maior limite : ")) 

## Retorna um número entre os x e y (Os 2 inclusos)
Rand = random.randint(Menor,Maior)

# Número mínimo de adivinhação = log 2 (limite superior - limite inferior + 1)
print("\n\t\tVocê tem apenas ", round(math.log(Maior - Menor + 1, 2))," chances para adivinhar o número!\n")

Tentativas = round(math.log(Maior - Menor + 1, 2))

Cont = 0

while Cont < Tentativas:
    Cont += 1

    Chute = int(input("Tente um número : ")) 
     
    if Rand == Chute:  
       print("Parabéns, você acertou em ", Cont, " tentativa(s)!!")
       
       break
    elif Rand > Chute:
       print("Arriscou um valor muito baixo...")
    elif Rand < Chute:
       print("Arriscou um valor muito alto...")
       
       
if Cont >= Tentativas:
    print("\n\tO número era %d."%Rand)
    print("\tBoa sorte na próxima vez !!")