from multiprocessing import Value
from optparse import Values
from random import*
import random



print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  L E T R A\n\n")
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    dataList=list(f)
    print()
    words=[]
    for line in dataList:
        words.append(line.strip().upper())
    #abre el archivo y lo pone en una variable es esta caso f 
    
    # print(dataList)
    #crea un dicionario(Tambien podria ser lista o tubla si ponemos el nombre)y lo enemura con enumerate 
    #y despues la variable y el numero donde arranca
    # print(real)
    valor=random.choice(dataList)
    # valor.strip().upper()
     #random().choice(nombre de la variable aqui) necesita los parentisis para poder funcionar por que es una clase        
     #esto seleciona random algo lista letra plabra etc
    print(valor)
    # para quitar los acentos a las palabras 
    valor2="".join(valor)
    print(valor2)
    new_sentence = valor2.maketrans('áéíóú', 'aeiou')
    n_valor = valor2.translate(new_sentence)
    print(n_valor)
    display=[]
    wordLen=len(n_valor)
    print(wordLen)
    for letter in n_valor:
        display += "_"
    print(display)

    while "_" in display:
        guessWord= input("Adivina la palabra \n").upper()

        for i in range(wordLen):
            word= n_valor[i]
            if word == guessWord:
                display[i]=word
        print(display)
        print(n_valor)
        if not "_" in display:
            print("you wow u are fanstastic")
        
        

   
          
   
def run ():
    pass


if __name__=="__main__":
    run()