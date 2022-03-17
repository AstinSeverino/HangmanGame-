from pickle import APPEND


def divisor (num1):
    divisor=[]
    for i in range (1,  num1+1):
        if num1 % i ==1:
            divisor.append(i)
    return divisor
    
def run ():
    try:
        num1= int(input('ingrese su numero para saber la multi'))
        if num1 <= 0:
            raise Exception('Negative number is not valid')
        print(divisor(num1))
        print('bye my friend')
    except ValueError:
        print("debe se un numero")


if __name__=='__main__':
    run()   
