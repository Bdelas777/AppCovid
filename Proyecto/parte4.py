from PIL import Image#Libreria para imprimir imágenes

def imprime_datos(opcion):
    '''Esta función nos muestra dado la opcion dada que lugar escogiste, la imagen del lugar para que el usuario la conozca,
    la dirección y nos muestra un mapa de su ubicación en Puebla '''
    if opcion==1:
        print('Escogiste: '),print('Arena BUAP')
        i=Image.open("BUAP.jpg",'r').show()
        print('Su dirección en: '),print('Av. del Polideportivo, Cd Universitaria, Universidades, 72589 Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("MAPABUAP.jpg",'r').show()
    elif opcion==2:
        print('Escogiste: '),print('Centro Expositor')
        i=Image.open("centro.jpg",'r').show()
        print('Su dirección en: '),print('Zona de los Fuertes, Cívica 5 de Mayo, 72260 Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("Mapacentro.jpg",'r').show()
    elif opcion==3:
        print('Escogiste: '),print('Hospital General Sur')
        i=Image.open("Hospital.jpg",'r').show()
        print('Su dirección en: '),print('Camino a Guadalupe Hidalgo 11350, Privada Agua Santa, Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("Mapahospital.jpg",'r').show()
    elif opcion==4:
        print('Escogiste: '),print('Unidad Deportiva VW')
        i=Image.open("deportiva.jpg",'r').show()
        print('Su dirección en: '),print('Recta a Cholula, Quetzalcoatl, 72760 San Andrés Cholula, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("mapadeportiva.jpg",'r').show()
    elif opcion==5:
        print('Escogiste: '),print('Universidad Anahuac')
        i=Image.open("anahuac.jpg",'r').show()
        print('Su dirección en: '),print('Av Orion Nte S/N, Tlaxcalancingo, Magisterio 2000 I, 72810 Tlaxcalancingo, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("mapaanahuac.jpg",'r').show()
    elif opcion==6:
        print('Escogiste: '),print('Tecnológico de Monterrey')
        i=Image.open("tec.jpg",'r').show()
        print('Su dirección en: '),print('Atlixcáyotl 5718, Reserva Territorial Atlixcáyotl, 72453 Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("mapatec.jpg",'r').show()
    elif opcion==7:
        print('Escogiste: '),print('Noveno Regimiento Blindado')
        i=Image.open("blindado.jpg",'r').show()
        print('Su dirección en: '),print('9/o. REGIMIENTO BLINDADO DE RECONOCIMIENTO, Claveles, Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("mapablindado.jpg",'r').show()
    elif opcion==8:
        print('Escogiste: '),print('Seminario Palafoxiano')
        i=Image.open("seminario.jpg",'r').show()
        print('Su dirección en: '),print('BACHILLERATO JOSÉ IGNACIO MÁRQUEZ. Prolongación de la 16 oriente s/n, El Porvenir C.P. 72330, Puebla, Pue.')
        print('Ubicado en un mapa es: ')
        i=Image.open("mapaseminario.jpg",'r').show()
    else:
        print('Esa opcion no es valida')
def sitio_vacuna():#Función principal que nos muestra el menú de la sección y nos dice que escojamos una opcion
    print('¿De qué centro de vacunación quiere saber? \n 1- Arena BUAP \n 2- Centro Expositor \n 3- Hospital General'+
          ' Sur\n 4- Unidad Deportiva VW \n 5- Universidad Anáhuac \n 6- Tecnológico de Monterrey \n'+
            ' 7- Segundo Regimiento Blindado \n 8- Seminario Palafoxiano \n')
    opcion=int(input())
    imprime_datos(opcion)#llamada a la función
