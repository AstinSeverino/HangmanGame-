from ast import Str
from multiprocessing import Value
from optparse import Values
from random import*
import random
import os

from sqlalchemy import false, true
endGame= False
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

os.system("clear")
print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  P A L A B R A\n\n")
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    dataList=list(f)
    # words=[]
    # for line in dataList:
    #     words.append(line.strip().upper())
    #abre el archivo y lo pone en una variable es esta caso f 
    
    # print(dataList)
    #crea un dicionario(Tambien podria ser lista o tubla si ponemos el nombre)y lo enemura con enumerate 
    #y despues la variable y el numero donde arranca
    # print(real)
    valor=random.choice(dataList)
    lisTen=[]
    for i in valor:
        lisTen.append(i.replace("\n", ""))
    lisTen.pop(-1) 
    # print(lisTen)
    # print(len(lisTen))
    # valor.strip().upper()
     #random().choice(nombre de la variable aqui) necesita los parentisis para poder funcionar por que es una clase        
     #esto seleciona random algo lista letra plabra etc
    # para quitar los acentos a las palabras 
    valor2="".join(lisTen)
    # print(valor2)
    new_sentence = valor2.maketrans('áéíóú', 'aeiou')
    n_valor = valor2.translate(new_sentence)
    # print(n_valor)

    display=[]

    
    words=[]
    for line in n_valor: 
        words.append(line.strip().upper())
    
        

    wordLen=len(words)
    # print(wordLen)
    for letter in words:
        display += "_"
    print(display)

    lives=7
    while lives>0 :
        
        guessWord= input(" A D I V I N A  L A  P A L A B R A \n \n").upper()

        for i in range(wordLen):
            word= words[i]
            if word == guessWord:
                os.system("clear")
                display[i]=word
                print("\n\n",display)
                
        if guessWord not in display:
            lives -=1
            os.system("clear")
            print("\n")
            print(display)
            print('T I E N E S  ', str(lives),"  ""V I D A S")
        if lives==6:
            print(stages[-1])
        elif lives==5:
            print(stages[-2])
        elif lives==4:
            print(stages[-3])
        elif lives==3:
            print(stages[-4])
        elif lives==2:
            print(stages[-5])
        elif lives==1:
            print(stages[-6])
        elif lives==0:
            print(stages[-7])

            if lives==0:
                endGame=True
                print("S E   T E R M I N I N O   E L   J U E G O" "\n \n ""L A  P A L A B R A   E R A --", n_valor.upper().strip(),"--")

                    
          
          
                    
        # if guessWord == True:
        #     pass
        # elif word!= guessWord: 
        #     print("T R Y ".upper())
        #     lives-1
        #     print("assci")
                
        # print("el final final")
        if not "_" in display:
            print("y o u   w o n   u   a r e   f a n s t a s t i c".upper())
            break
        
        

   
          
   
def run ():
    pass


if __name__=="__main__":
    run()