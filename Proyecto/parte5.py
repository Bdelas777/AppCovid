from PIL import Image#Liberia que nos sirve para poner imágenes
import matplotlib.pyplot as plt#Libreria que sirve para hacer gráficas
def imprime_datos(opcion):
    if opcion==1:
        print('Escogiste: '),print('Hospital Puebla')
        i=Image.open("hpuebla.jpg",'r').show()
        print('Se ubica en: '),print('Priv. de las Ramblas 4, Reserva Territorial Atlixcáyotl,',
            'Corredor Comercial Desarrollo Atlixcayotl, 72197 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [56,44]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital Puebla')
        plt.show()
    elif opcion==2:
        print('Escogiste: '),print('Hospital Ángeles')
        i=Image.open("angeles.jpg",'r').show()
        print('Se ubica en: '),print(' Av. Kepler 2143, Reserva Territorial Atlixcáyotl, 72190 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [54,46]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital Ángeles')
        plt.show()
    elif opcion==3:
        print('Escogiste: '),print('Hospital de Especialidades(ISSSTEP)')
        i=Image.open("esp.jpg",'r').show()
        print('Se ubica en: '),print('72550, Av Emiliano Zapata 4730, San Baltazar Campeche, 72550 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [62,38]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital de Especialidades')
        plt.show()
    elif opcion==4:
        print('Escogiste: '),print('Hospital Universitario de Puebla')
        i=Image.open("hbuap.jpg",'r').show()
        print('Se ubica en: '),print('Av 27 Pte, Los Volcanes, 72410 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [50,50]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital Universitario de Puebla')
        plt.show()
    elif opcion==5:
        print('Escogiste: '),print('Hospital Betania')
        i=Image.open("betania.jpg",'r').show()
        print('Se ubica en: '),print('Av 11 Ote 1826, Azcarate, 72501 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [46,54]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital Betania')
        plt.show()
    elif opcion==6:
        print('Escogiste: '),print('Hospital Beneficencia Española')
        i=Image.open("espe.jpg",'r').show()
        print('Se ubica en: '),print(' Calle 19 Nte. 1001, Jesús García, 72090 Puebla, Pue.')
        etiquetas = ['Camas no disponibles','Camas disponibles']
        valores = [56,44]
        colores = ['#ff4500','#7bb0ff']
        plt.pie(x=valores, labels=etiquetas, colors = colores, autopct="%0.1f %%", shadow=True)
        plt.title('Disponibilidad en el Hospital Beneficencia Española')
        plt.show()
    else:
        print('Esa opcion no es valida')
        
def hospitales():
    #Funcion que nos dice el menu a escoger y le pide al usuario una opcion
    print('¿De que Hospital quieres saber? \n 1- Hospital Puebla \n 2- Hospital Ángeles \n 3- Hospital de Especialidades'+
    '\n 4- Hospital Universitario de Puebla \n 5- Hospital Betania \n 6- Hospital Beneficencia Española \n')
    opcion=int(input())
    imprime_datos(opcion)#llamada a la función