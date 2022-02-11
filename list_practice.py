def run ():
    valos = []   
    

    # # number = [i for i in range(1, 100000) if i % 36 == 0]

    # for i in range (1, 100000):
    #     if i % 36 != 0:
    #         return i
    #     print(valos)
    #     break
             

    # # print(number)
    for i in range (0, 10000):
        if i % 4 ==0 and i % 6==0 and i % 9==0:
            print(i) 
#primer resultado de la vuelta al uso de python 
#aun nose usar returm 

if __name__=='__main__':
    run()
