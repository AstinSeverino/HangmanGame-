from random import*
import random
import os

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
# limpia la pantalla de la terminal en unix
os.system("clear")
print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  P A L A B R A\n\n")
# Abre un archibo lee la info y la guarda en una variable 
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    dataList=list(f)
# Seleciona una palbra de la lista, le quita el salto de linea un salto de linea que tenia al final
    valor=random.choice(dataList)
    lisTen=[]
    for i in valor:
        lisTen.append(i.replace("\n", ""))
    lisTen.pop(-1) 
    #Quita los espacios de los string y para quitar los acentos a las palabras 
    valor2="".join(lisTen)
    new_sentence = valor2.maketrans('áéíóú', 'aeiou')
    n_valor = valor2.translate(new_sentence)
# Agrega las palabras a un str sin espacion y en mayus 
    display=[]
    words=[]
    for line in n_valor: 
        words.append(line.strip().upper())       
    wordLen=len(words)
# Imprime los los quiones de la letra en la pantalla 
    for letter in words:
        display += "_"
    print(display)
# Sistema de vidas
    lives=7
    while lives>0 :
        
        guessWord= input(" A D I V I N A  L A  P A L A B R A \n \n").upper()
# Comprueba si la latra es la que entro el usuario si es asi la agrega a la lista para mosntrar
# si no esta procede con el bucle 
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

        if not "_" in display:
            print("y o u   w o n   u   a r e   f a n s t a s t i c".upper())
            break
        
def run ():
    pass


if __name__=="__main__":
    run()   