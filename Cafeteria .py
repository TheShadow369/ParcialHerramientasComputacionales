"""
Cafeteria unijave
"""
def totales(li):
    i,fal,des = 0 , 0 , 0
    tot = 0
    to_des = 0
    while i < len(li)-1:
        tot += (li[i][3] * li[i][2])
        i+=1
 
    if fal == 3:
        print("Maximo de Errores alcanzado")
        return False
    if li[len(li)-1] == "estudiante":
        print("Tiene Beca, escriba yes o no")
        com = input().lower()
        if com != "yes" and com != "no":
            fal+=1
            print("Respuesta invalida intentelo de nuevo")
            com = input().lower()
        elif com == "yes":
            des = 50
            to_des = tot - (tot * 0.50)
        else:
            des = 30
            to_des = tot - (tot * 0.30)
            
    elif li[-1] == "profesor":
        des = 20
        to_des = tot - (tot * 0.20)
        
    else:
        to_des = tot
    return (tot,des,to_des)

def factura(lis,tu, cedu):
    print()
    print()
    print("                  ....Factura Unijave....                ")
    print("  ",lis[-1], "identificado con el documento", cedu)
    for i in range(len(lis)-1):
        to = lis[i][3] *  lis[i][2]
        print(" Codigo", *lis[i][1], "      ",lis[i][0],"     ",lis[i][2],"      ", lis[i][3],"     " , to )

    print("  Total :  ", tu[0],"$    ")
    print("  Descuento aplicado" , tu[1],"%")
    print("  Total a pagar   %.2f" %tu[2], " $")
    print()
    print()
     

program = True
while program == True:
    dic = {}
    menu = """
                              Restaurante Uni-Jave

                            1. Venta
                        
                            0. Cerrar 
                _______________________________________________

"""
    print(menu)
    opcion = input("Seleccione Opción Requerida :  ")
    if opcion == "1":
        errores = 0
        com = []
        ban = True
        print("Ingrese Producto : " , end = "")
        pro = input().lower()
        if len(pro) == 0:
            ban = False
            print(menu)
            opcion = input("Seleccione Opción Requerida :  ")
        if errores == 3:
            print(menu)
            opcion = input("Seleccione Opción Requerida :  ")
        while ban == True:
            cod = input("Ingrese codigo del producto: ")
            if cod.isdigit() == True and len(cod) == 4:
                precio = input("Ingrese precio del producto: ")
                if precio.isdigit() and len(precio) <= 8:
                    can = input("Ingrese cantidad a llevar: ")
                    if can.isdigit() and 0 < len(can) <= 3:
                        dic[cod] = (pro,int(precio))
                        com.append([pro,cod,int(can),int(precio)])
                        print("Ingrese Producto : " , end = "")
                        pro = input().lower()
                        if len(pro) == 0:
                            ban = False
                    else:
                        errores+=1
                        print("Invalido")
                        can = input("Ingrese cantidad a llevar : ")
                else:
                    errores+=1
                    print("Invalido")
                    precio = input("Ingrese Precio del producto : ")
            else:
                errores+=1
                print("Codigo solo debe tener 5 Caracteres Numericos")
                cod = input("Ingrese codigo del producto")
                      
        
        per = input("Ingrese tipo de cliente :").lower()
        docu = input("Ingrese Documento :")
        com.append(per)
        res = totales(com)
        if res == False:
            print(menu)
            opcion = input("Seleccione Opción Requerida :  " )
        else:
            factura(com,res,docu)
            print(menu)
            opcion = input("Seleccione Opción Requerida :   ")
        

        
    elif opcion == "0":
        print("Cerrando")
        program = False
        
    else:
        print("Invalido")
        opcion = input("Seleccione Obcion Requerida :  ")
        
        
