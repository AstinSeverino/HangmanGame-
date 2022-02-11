def run(): 
    realDic2 = {}


#     realDict = {i: i**2 for i in range (1, 100) if i >0}
# # diccionaio comprehersion que es una lines y funciona el codigo 
# #ahora hacerlo normal 
    for i in range (1, 100):
        if 1**2 > 0:
            realDic2[i] = i**2

#aqui lo hicimos con con el normal que es lo mismo que la otra 
    print(realDic2)
if __name__=='__main__':
    run()