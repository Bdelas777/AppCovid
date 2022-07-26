#--------Importamos las librerías pil y matplotlib para poder usarlas para meter imágenes y graficas respectivamente
from PIL import Image
#import matplotlib.pyplot as plt# le decimos que la librería se llame plt para acortarlo

def sacar_datossemaforo(): #Función que nos permite extraer los datos de un archivo en este caso txt
    matriz=[] #matriz a guardar
    f=open("semaforo.txt","r") #abrimos el archivo en modo lectura
    for linea in f: #Extración de la información
        wordlist=linea.split()
        matriz.append(wordlist)
    f.close() #cerramos el archivo
    return matriz #devolvemos la matriz para poder usarla en el resto del código

def colorsemaforo(matriz,opcion):
    '''Función que nos dice el semáforo del estado, el comparativo de todos los y a qué porcentaje de ese
    estados a que comparativo pertenece'''
    #Le decimos el color del semáforo del estado usando la opción para conocer la columna y el otro es 3 porque es
    # la fila en cuál se encuentra
    print('Que tiene un color de semáforo de',matriz[opcion][3])#Usamos el if para imprimirle el color del semáforo
    # y checa cuál opción coincide con la de la base de datos
    if matriz[opcion][3]=='Verde':
        img = Image.new("RGB", (250,250), (0,255,0))
        img.show()
    elif matriz[opcion][3]=='Amarillo':
        img = Image.new("RGB", (250,250), (255,255,0))
        img.show()
    else:
        img = Image.new("RGB", (250,250), (239,127,26))
        img.show()
    print('El comparativo con los otros estados es: ')#Le informamos que vamos a comparar con otros estados
    #------------------------Acumuladores que van a guardar cuantas veces sale la respectiva palabra---------
    verde=0
    amarillo=0
    naranja=0
    #Con estos for vemos cuantas veces sale el color en la matriz y lo guardamos para usarlo en la gráfica
    for i in range(32):
        for j in range(3,4):
            if matriz[i][j]=='Verde':
                verde+=1
            elif matriz[i][j]=='Amarillo':
                amarillo+=1
            else:
                naranja+=1
    #Creación de la gráfica de pastel con la librería matplotlib.pyplot dado etiquetas, valores y colores
    etiquetas = ['Verde','Amarillo','Naranja']
    valores = [verde,amarillo,naranja]
    colores = ['green','yellow','orange']
    plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
    plt.title('Comparativo del semáforo con todos los estados')
    plt.show()
    #If que saca el promedio por el color dependiendo del color que diga en la base de datos
    if matriz[opcion][3]=='Verde':
        total=verde/32
    elif matriz[opcion][3]=='Amarillo':
        total=amarillo/32
    else:
        total=naranja/32
    #Nos dice en que porcentaje de la gráfica parte del porcentaje está el estado escogido
    print('El estado de',matriz[opcion][1],'está en el  porcentaje de',round(total*100,1),' %')
    
def haz_barras(listanombre,listacasos):#Función que nos crea la gráfica de barras dados el eje_x y eje_y para no
    #porque se usa demasiado en el código
    eje_x = listanombre
    eje_y = listacasos
    plt.figure(figsize=(12,4))
    plt.bar(eje_x, eje_y)
    plt.ylabel('Casos por estado') 
    plt.xlabel('Nombre del estado')
    plt.title('Números de casos por estado')
    plt.show()
    
def casos_covid(matriz,opcion):#Función que crea lo gráficos de barra, te da el máximo y mínimo de casos y promedio
    print('Su número de casos es: ',matriz[opcion][2])#le informamos el número de casos del estado
    #Creamos unas listas que usaremos más adelante
    listanombre=[]
    listacasos=[]
    #Guardamos los nombres y el número de casos en las listas para usarlos en los ejes x y y respectivamente al 
    # crear el gráfico
    for i in range(32):
        for j in range(1,3):
            numero=int(matriz[i][2])
            if j==1:
                listanombre.append( matriz[i][1])
            if j==2:
                listacasos.append(numero)
    print('Comparativo con otros estados: ')
    '''Creación de 4 ciclos for para poder crear 4 gráficos dividiendo las listas en 4 partes para mandárselas al
     eje x y y, de ahí las vaciamos para poder utilizarlas con otros valores'''
    listanombretemporal=[]
    listacasostemporal=[]
    for i in range(8):
        listanombretemporal.append(listanombre[i])
        listacasostemporal.append(listacasos[i])
    haz_barras(listanombretemporal,listacasostemporal)
    listanombretemporal=[]
    listacasostemporal=[]
    for i in range(8,16):
        listanombretemporal.append(listanombre[i])
        listacasostemporal.append(listacasos[i])
    haz_barras(listanombretemporal,listacasostemporal)
    listanombretemporal=[]
    listacasostemporal=[]
    for i in range(16,24):
        listanombretemporal.append(listanombre[i])
        listacasostemporal.append(listacasos[i])
    haz_barras(listanombretemporal,listacasostemporal)
    listanombretemporal=[]
    listacasostemporal=[]
    for i in range(24,32):
        listanombretemporal.append(listanombre[i])
        listacasostemporal.append(listacasos[i])
    haz_barras(listanombretemporal,listacasostemporal)
    '''Conclusiones de los gráficos observados, es decir, promedio a nivel país, estado con mayor y menores casos y
    en lugar ocupa el estado escogida en cuanto a los estados con menores casos'''
    print('Después de ver  estos gráficos podemos concluir que: ')
    print('El promedio de los casos en todo el país es de',round(sum(listacasos)/32,2))
    print('El mayor número de casos es',max(listacasos),'en',matriz[9][1])
    print('El mayor número de casos es',min(listacasos),'en',matriz[6][1])
    listacasos.sort() #Ordenamiento de lista
    numero=int(matriz[opcion][2]) # guardamos en una variable los datos como int porque la matriz al extraerlo del
    #archivo lo toma como caracteres
    a=0#Va contando en que para ver en qué lugar va a salir el estado
    for i in listacasos:
        a+=1
        if i==numero: #checamos si es el valor de matriz es igual en la lista ordenada para poder imprimirlo
            print('El estado de',matriz[opcion][1],'con un número de casos de',matriz[opcion][2],'está en el lugar',
                  a,'de 32 de pacientes con menos casos de COVID')
            break #Rompemos el código porque los demás datos no nos interesan
        
def graficas(): #función principal de la parte 1 que llama a las otras funciones y guarda a la matriz
    matriz=sacar_datossemaforo()#llamamos a esa función para poder usar la matriz en esta función y en las otras creadas
    print('Dame el número del estado del 1 al 32: ')#le pedimos al usuario el número del estado ya que lo usaremos como para saber 
    #la columna de la matriz que nos será útil en las funciones colorsemaforo y casos_covid
    for i in range(32):#Este ciclo imprime el número y el nombre del estado
        for j in range(2):
            print(matriz[i][j],end=" ")
        print()
    opcion=int(input())#este número guarda el numero del estado
    while opcion>32 :#Checa que la opcion sea de 1 al 32
        opcion=int(input('Introduce una opción del 1 al 32: '))
    opcion-=1#le quitamos uno porque recordamos que Python cuenta de 0 a n-1
    print('El estado que escogiste fue',matriz[opcion][1] )#Le informamos al usuario de su selección
    #llamada a las funciones dado la matriz y opcion escogida
    colorsemaforo(matriz,opcion)
    casos_covid(matriz,opcion)