def sacar_datosdeamigosytelefonos():#Función que nos permite extraer los datos de un archivo en este caso txt
    matriz=[]#matriz a guardar
    f=open("amigostelefonos.txt","r")#abrimos el archivo en modo lectura
    for linea in f:#Extracion de la información
        wordlist=linea.split()
        matriz.append(wordlist)
    f.close()#cerramos el archivo
    return matriz #devolvemos la matriz para poder usarla en el resto del código

def cambio_datos_envio_mensaje(matriz,nombre):
    for i in range(40):
        for j in range(1): #Usamos uno porque esa es la columna del nombre de usuario
            if nombre==matriz[i][0]: #checamos en que posición esta
                #Imprimos la información del usuario y los contactos
                print( "f El usuario llamado {nombre}")
                print('Sus contactos son: ')
                print('Amigo 1:',matriz[i][1],'Teléfono:',matriz[i][2])
                print('Amigo 2:',matriz[i][3],'Teléfono:',matriz[i][4])
                print('Amigo 3:',matriz[i][5],'Teléfono:',matriz[i][6])
                pregunta=input('¿Quiere modificar algún dato? si/no ')#Checamos si quiere cambiar algún dato
                pregunta.lower() #Lo hacemos con minúsculas para asegurar que el dato sea correcto
                '''Aquí le decimos al usuario que, si quieres modificar algo, de ser así le pregunta por el amigo 1,2 y 3
                , le pregunta si quiere modificar nombre, teléfono o ambos  y te imprime la matriz modificada'''
                if pregunta=='si':
                    cambio=input('¿Que desea modificar algo del  amigo 1? si/no ')
                    cambio.lower()
                    if cambio=='si':
                        cosa_cambiada=input('Introduzca: nombre/teléfono/ambos ')
                        cosa_cambiada.lower()
                        if cosa_cambiada=='nombre':
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][1]=nombre
                        elif cosa_cambiada=='telefono':
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][2]=telefono
                        else:
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][1]=nombre
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][2]=telefono
                    cambio=input('¿Que desea modificar algo del  amigo 2? si/no ')
                    cambio.lower()
                    if cambio=='si':
                        cosa_cambiada=input('Introduzca: nombre/teléfono/ambos ')
                        cosa_cambiada.lower()
                        if cosa_cambiada=='nombre':
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][3]=nombre
                        elif cosa_cambiada=='telefono':
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][4]=telefono
                        else:
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][3]=nombre
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][4]=telefono
                    cambio=input('¿Que desea modificar algo del  amigo 3? si/no ')
                    cambio.lower()
                    if cambio=='si':
                        cosa_cambiada=input('Introduzca: nombre/teléfono/ambos ')
                        cosa_cambiada.lower()
                        if cosa_cambiada=='nombre':
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][5]=nombre
                        elif cosa_cambiada=='telefono':
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][6]=telefono
                        else:
                            nombre=input('Introduzca el nuevo nombre: ')
                            matriz[i][5]=nombre
                            telefono=int(input('Introduzca el nuevo teléfono: '))
                            matriz[i][6]=telefono
                    print('Los contactos modificados fueron: ')
                    print('Amigo 1:',matriz[i][1],'Teléfono:',matriz[i][2])
                    print('Amigo 2:',matriz[i][3],'Teléfono:',matriz[i][4])
                    print('Amigo 3:',matriz[i][5],'Teléfono:',matriz[i][6])
                '''Aquí le preguntamos al usuario si quiere mandar un mensaje, de ser así le dice cual quiere y le
                confirma que tal mensaje se envió'''
                mandar_mensaje=input('¿Desea mandarles un mensaje a sus contactos? si/no ' )
                mandar_mensaje.lower()
                if mandar_mensaje=='si':
                    mensaje=input('Dime el mensaje: ')
                    print('El mensaje que es',mensaje,'se ha enviado')
            break#Rompemos el código porque la demás información no nos interesa
            
def mensajes(nombre):#función principal de la parte 2 que llama a las otras funciones ,guarda a la matriz
     #y pide el nombre que pedimos en el min principal porque se va a usar
    matriz=sacar_datosdeamigosytelefonos()
    #llamamos a esa función para poder usar la matriz en esta función y en las otras creadas
    #llamada a las funciones dado la matriz y nombre del usuario
    cambio_datos_envio_mensaje(matriz,nombre)
