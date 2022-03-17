from pickle import APPEND


def divisor (num1):
    divisor=[]
    for i in range (1,  num1+1):
        if num1 % i ==1:
            divisor.append(i)
    return divisor
    
def run ():
    

    num1=(input('ingrese su numero para saber la multi')) 
    assert num1.isnumeric() and  int(num1)>=0, "ingrese un numero positivo y no letras "
    # assert num1 <=0, "el numero debe ser positivo"
    print(divisor(int(num1)))
    print('bye my friend')
    
if __name__=='__main__':
    run()   
