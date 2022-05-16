from random import*


# def read():
    # words=[]
    # with open("./archivos/data.txt", "r", encoding="utf-8") as f:
    #     return f 
        #utd-8 es para corregir el texto en espanol y na tilde y eso    
    #     for line in f:
    #         # f.w("\n")
    #         words.append(line) 
    # print(words)        


def proData():
   
    # f =["calor", "perro", "ejpss", "psdns"]
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
        valor=dict(enumerate(valor,1))
        comprobador
        print(valor)
        print(len(valor)) 
        print(" _ " * len(valor))

def comprobador():
    verificar= input("INTRUCE LA LETRA")
    valor.get(verificar, "no se encontro")

   
          
   
def run ():
    pass


if __name__=="__main__":
    proData()