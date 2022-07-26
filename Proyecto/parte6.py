def contesta_encuesta(positivo): #Esta función esta creada para omitir 5 linea de código con lo mismo trata de
    #preguntar si la respuesta le agregue a positivo uno y pide positivo para modificarlo y luego devolverlo
    #modificado
    duda=input()
    duda=duda.lower()
    if duda=='si':
        positivo+=1
    return positivo
        
def sintomas():#Funciona que te pregunta posibles síntomas y si es mayor o igual a 5 en el acumulador los síntomas 
    #entonces eres sospechoso sino solo te dice que te cuides
    positivo=0#acumulador
    #Serie de preguntas
    print('1- ¿Ha tenido fiebre?, es decir mayor a 37.5 grados si/no ')
    positivo=contesta_encuesta(positivo)
    print('2- ¿Ha tenido tos? si/no ')
    positivo=contesta_encuesta(positivo)
    print('3- ¿Te cuesta respirar? si/no ')
    positivo=contesta_encuesta(positivo)
    print('4- ¿Has estado con alguien que tiene o tuvo coronavirus? si/no ')
    positivo=contesta_encuesta(positivo)
    print('5- ¿Tienes mocos? si/no ')
    positivo=contesta_encuesta(positivo)
    print('6- ¿Te duelen los músculos? si/no ')
    positivo=contesta_encuesta(positivo)
    print('7- ¿Tienes malestar general? si/no ')
    positivo=contesta_encuesta(positivo)
    print('8- ¿Vives con muchas personas o en una residencia? si/no ')
    positivo=contesta_encuesta(positivo)
    print('9- ¿Tienes vomito o diarrea? si/no ')
    positivo=contesta_encuesta(positivo)
    print('10- ¿Has pérdido el olfato o el gusto? si/no ')
    positivo=contesta_encuesta(positivo)
    #if que te dice si eres sospechoso o no
    if positivo>=5:
        print('Eres sospechoso de COVID, por favor aíslate y hazte la prueba de COVID')
    else:
        print('No eres sospechoso de COVID, sin embargo, síguete cuidado')     
