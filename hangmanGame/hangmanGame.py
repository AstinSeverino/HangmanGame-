from multiprocessing import Value
from optparse import Values
from random import*



print("\nC O M I E N Z A  E L J U E G O \n A D I V I N A  L A  L E T R A\n\n")
with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    #abre el archivo y lo pone en una variable es esta caso f 
    dataList=dict(enumerate(f,1))
    #crea un dicionario(Tambien podria ser lista o tubla si ponemos el nombre)y lo enemura con enumerate 
    #y despues la variable y el numero donde arranca
    realDataList=dataList
    # print(real)
    valor=Random().choice(realDataList)
     #random().choice(nombre de la variable aqui) necesita los parentisis para poder funcionar por que es una clase        
     #esto seleciona random algo lista letra plabra etc
    print(valor)
    valor=dict(enumerate(valor))
    print(valor)
    verificar= input("INTRUCE LA LETRA ")# me quede probando con el metodo get para ver si puede verificar si las letra que entra el usuario estan ahi 
    # print(valor.get("verificar","El valor no se encuentra en el dic"))
    for i in valor.get(i):
        if i == verificar:
            print("som igaules")
        else:
            print("no so iguales")
        # if valor == verificar: 
            # print(valor.get(i,"no esta"))
    # print(valor)
    # print(len(valor)) 
    # print(" _ " * len(valor))

    

   
          
   
def run ():
    pass


if __name__=="__main__":
    run()