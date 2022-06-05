from multiprocessing import Value
from optparse import Values
from random import*
import random
# from string import maketrans



print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  L E T R A\n\n")
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    words=[]
    for line in f:
        words.append(line.strip().upper())
    #abre el archivo y lo pone en una variable es esta caso f 
    # dataList=list(f)
    # print(dataList)
    #crea un dicionario(Tambien podria ser lista o tubla si ponemos el nombre)y lo enemura con enumerate 
    #y despues la variable y el numero donde arranca
    # print(real)
    valor=random.choice(words)
    # valor.strip().upper()
     #random().choice(nombre de la variable aqui) necesita los parentisis para poder funcionar por que es una clase        
     #esto seleciona random algo lista letra plabra etc
    print(valor)
    #para quitar los acentos a las palabras 
    intab="áéíóú"
    outtab="aeiou"
    new_sentence =valor.maketrans(intab, outtab)
    n_valor = (valor.translate(new_sentence))
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
        
        

def prueba():
    sentence = "Mi mamá"
    #"Mi mamá le compró un balón de fútbol a mi hermano"

    new_sentence = sentence.maketrans('áéíóú', 'aeiou')
    n_sentence = sentence.translate(new_sentence)
    print(n_sentence)
    test=input("introduce algo")
    if n_sentence == test:
        print("funciona")
    else:
        print("no funciono")
    
 
          
   
def run ():
    prueba()


if __name__=="__main__":
    run()