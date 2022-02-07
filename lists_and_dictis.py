# from typing_extensions import TypeGuard


from typing import ItemsView


def run():
    my_list = [1, 3, "hanksnak", True, 4.553]
    my_dic = {"hey you", 34, False, 435.664}

    super_list =[
        {"fistname": "maria", "lastname": "herrera"},
        {"fistname": "maria", "lastname": "garcia"},
        {"fistname": "papo", "lastname": "purer"},
        {"fistname": "tatoa", "lastname": "garcia"},
        
    ]

    super_dict = {
        "natural_num": [35, 2, 4, 5],
        "natural_num": [90, 3, 4, 5],
        "natural_num": [9, 25, 4, 5],
        "natural_num": [8, 64, 4, 5],
    }
    for key, value in super_dict.items():
        print(key, "-", value)
    

    # for values in super_list:
    #     # print(items)
    #     for key, value in value.items():
    #         print(f'{key}-{value}')

    for i in super_list:
        for key, values in i.items():
            print(key,": ", values);
            #esto es para imprimir las listas que contiene dicionario pero despues 
            #hay que imprimir los dicionarios  en su forma

if __name__=='__main__':
    run()