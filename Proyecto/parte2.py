#--------Importamos las librerías pil y matplotlib para poder usarlas para meter imágenes y graficas respectivamente
from PIL import Image
import matplotlib.pyplot as plt# le decimos que la librería se llame plt para acortarlo
def sacar_datosdevacunados():#Función que nos permite extraer los datos de un archivo en este caso txt
    matriz=[]#matriz a guardar
    f=open("vacunados.txt","r")#abrimos el archivo en modo lectura
    for linea in f:#Extracion de la información
        wordlist=linea.split()
        matriz.append(wordlist)
    f.close()#cerramos el archivo
    return matriz#devolvemos la matriz para poder usarla en el resto del código

def datos_vacunados(matriz,nombre):#Función que nos dice la información si estas vacunado o no, y de ser así nos dice
    #las fechas de vacunación
    for i in range(40):
        for j in range(1):#Usamos uno porque esa es la columna del nombre de usuario
            if nombre==matriz[i][0]:#checamos en que posición esta
                print(f'El usuario llamado {nombre}')#Esto nos indica su posición
                opcion=matriz[i][1]#Este nos indica que si esta vacunado o no
                opcion=opcion.lower()
                #Usamos lower porque no sabemos cómo vienen los si o no en la función y así aseguramos
                if opcion=='si':#si esta vacunado le decimos de que marca y dependiendo de la vacuna sus fechas de
                    #vacunacion
                    print('Si esta vacunado')
                    print('Su marca de vacuna es',matriz[i][2])
                    marca=matriz[i][2]
                    if marca=='Johnson&johnson':
                        print('Al ser la marca ',marca,'por eso solo tuvo una dosis el día',matriz[i][3])
                    else:
                        print('Al ser la marca',marca,'por eso solo tuvo dos dosis los días',matriz[i][3],'y',
                          matriz[i][4])
                else:#Sabemos que no está vacunado
                    print('No esta vacunado')
                break #Rompemos el código porque la demás información no es interesante
            
def grafico_vacunados(matriz,nombre):
    '''Función que nos dice el comparativo de la vacunación de los usuarios por marca y de vacunados y no vacunados'''
    #------------------------Acumuladores que van a guardar cuantas veces sale el tipo de marca--------
    pfizer=0
    astra=0
    moderna=0
    johnson=0
    sputnik=0
    sindatos=0
    #Con estos for vemos cuantas veces sale la marca en la matriz y lo guardamos para usarlo en la grafica
    for i in range(40):
        for j in range(2,3):
            if matriz[i][j]=='Pfizer':
                pfizer+=1
            elif matriz[i][j]=='Astra_Seneca':
                astra+=1
            elif matriz[i][j]=='Moderna':
                moderna+=1
            elif matriz[i][j]=='Johnson&johnson':
                johnson+=1
            elif matriz[i][j]=='Sputnik':
                sputnik+=1
            else:
                sindatos+=1
    #Creación de la grafica de pastel con la librería matplotlib.pyplot dado etiquetas, valores y colores
    etiquetas = ['Pfizer','Astra Seneca','Moderna','Johnson & Johnson','Sputnik','No sean vacunado']
    valores = [pfizer,astra,moderna,johnson,sputnik,sindatos]
    colores = ['#2b31b2','#d3d85d','#ba38cf','#dda173','#872121','#36b22b']
    plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
    plt.title('Comparativo de vacunación de marcas o no vacunados por todos los usuarios')
    plt.show()
    total=pfizer+astra+moderna+johnson+sputnik#Suma de las marcas para saber el porcentaje de vacunados
    #Creación de la grafica de pastel con la librería matplotlib.pyplot dado etiquetas, valores y colores
    etiquetas = ['Gente vacunada','Gente sin vacunar',]
    valores = [total,sindatos]
    colores = ['#2b31b2','#d3d85d']
    plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
    plt.title('Comparativo de usuarios vacunados o no')
    plt.show()
    #Impresion de las conclusiones del grafico anterior
    print('Como podemos ver hubo un mayor porcentaje de vacunados en nuestros usuarios con',round(total/40*100,2),'%')
    print('Sin embargo hay un alto porcentaje de no vacunados con',round(sindatos/40*100,2),'%')
'''función principal de la parte 2 que llama a las otras funciones, guarda a la matriz
     y pide el nombre que pedimos en el main principal porque se va a usar'''

def info_vacunados(nombre):
    matriz=sacar_datosdevacunados()
    #llamamos a esa función para poder usar la matriz en esta función y en las otras creadas
    #llamada a las funciones dado la matriz y nombre del usuario
    nombre=datos_vacunados(matriz,nombre)
    grafico_vacunados(matriz,nombre)
