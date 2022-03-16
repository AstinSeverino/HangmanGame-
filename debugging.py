from pickle import APPEND


def divisor (num1):
    divisor=[]
    for i in range (1,  num1+1):
        if num1 % i ==1:
            divisor.append(i)
    return divisor
def run ():
    num1= int(input('ingrese su numero para saber la multi'))
    print(divisor(num1))
    print('bye my friend')



if __name__=='__main__':
    run()   
