
def read():
    number=[]
    with open("./archivos/number.txt", "r", encoding="utf-8") as f:
        #utd-8 es para corregir el texto en espanol y na tilde y eso    
        for line in f:
            number.append(int(line))  
    print(number)        


def write(): 
    names = ["carlos","astin", "sasalks","kskks", "jose", "rene" ,"corre"]
    with open("./archivos/number.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
            #para hacer un salto de linea 




def run():
    write()



if __name__=='__main__':
    run()