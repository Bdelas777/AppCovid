#Autores: Bernardo de la Sierra Rábago y Ana Cristina Menéndez Montiel
#--------------------------------------------Importación de funciones----------------------------------------
'''En este apartado importamos las librerías que creamos para poder usarlas y dividir el código por partes para
facilitar su lectura, corrección de errores y más adelante poder mejorar el código en una zona específica'''
from entrada import sacar_datos,checar_datos
from parte1 import graficas
from parte2 import info_vacunados
from parte3 import mensajes
from parte4 import sitio_vacuna
from parte5 import hospitales
from parte6 import sintomas
#---------------------------------Aquí hicimos la función principal que hará que corra el programa-------------
def menu():#Función que nos imprime el menú de opciones
    print('A continuación se te presentaran una serie de opciones: \n 1- Dime el semáforo \n 2- '+
        'Verificación de Vacuna \n 3- Cambiar tus contactos o notificarles algo \n 4- ¿Dónde vacunarme? \n '+
        '5- Hospitales \n 6- Síntomas \n 7- Salir ')
def main():#Función principal
    entrada=False #Aqui declaramos una centinela para poder hacer un ciclo que se corra hasta que el usuario quiera
    contador_intentos=0 #contador de intentos de entrada del usuario
    while entrada==False:
        nombre=input('Introduce tu nombre de usuario: ')#Pedimos el nombre del usuario porque mas adelante lo 
        # usaremos además de usarlo para poder acceder en la parte 2 y 3 del código
        nombre=nombre.capitalize()#con capitaliza nos aseguramos que el usuario sea mayúscula al inicio y lo demás
        #minúsculas para así evitar errores al entrar si el usuario lo digita mal
        entrada=checar_datos(entrada,nombre) #llamada a la función que nos deja acceder ver en entrada.py
        if(entrada==True): #Entrada al sistema
            print('Bienvenido al sistema')#Nos notifica que estas en el sistema
            menu()#llamada a la función menú
            opcion=int(input('Escoja su opcion: '))#le pedimos la opción
            while opcion!=7:#While que nos permitirá seguir en el ciclo hasta que el usuario quiera salir
                #llamadas de funcion en las respectivas partes del codito
                if opcion==1:
                    graficas()#función principal de la parte 1
                elif opcion==2:
                    info_vacunados(nombre)#función principal de la parte 2
                elif opcion==3:
                    mensajes(nombre)#función principal de la parte 3
                elif opcion==4:
                    sitio_vacuna()#función principal de la parte 4
                elif opcion==5:
                    hospitales()#función principal de la parte 5
                elif opcion==6:
                    sintomas()#función principal de la parte 6
                elif opcion==7:
                    break #Rompimiento del código
                else:
                    print('opción invalida')#Nos dice que no pusiste una opción que estaba en el menú      
                menu()#llamada a función y pedida de opción
                opcion=int(input('Escoja su opcion: '))
        else:#esta excepción checa que si no eres usuario y va quitando intentos hasta llegar 0 y
            print('Vuelve a intentarlo, algo está mal')
            contador_intentos+=1
            print(f"Te quedan {3-contador_intentos} intentos")
            if contador_intentos==3:
                print('Inténtalo en 20 minutos')
                break
    print('Gracias por usar esta aplicación')#Nos informa que te has salido del programa
main()#llamada a la función principal 