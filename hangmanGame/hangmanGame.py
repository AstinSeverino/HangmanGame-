from multiprocessing import Value
from optparse import Values
from random import*



print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  L E T R A\n\n")
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    #abre el archivo y lo pone en una variable es esta caso f 
    dataList=list(f)
    #crea un dicionario(Tambien podria ser lista o tubla si ponemos el nombre)y lo enemura con enumerate 
    #y despues la variable y el numero donde arranca
    # print(real)
    valor=Random().choice(dataList)
     #random().choice(nombre de la variable aqui) necesita los parentisis para poder funcionar por que es una clase        
     #esto seleciona random algo lista letra plabra etc
    print(valor)
    display=[]
    wordLen=len(valor)-1
    for letter in valor:
        display += "_"
    print(display)

    while '_' in display:
        guessWord= input("Adivina la palabra").lower()

        for i in range(wordLen):
            word= valor[i]
            if word == guessWord:
                display[i]=word
        print(display)
        print(valor)
        if not "_" in display:
            print("you wow u are fanstastic")
        
        

   
          
   
def run ():
    pass


if __name__=="__main__":
    run()