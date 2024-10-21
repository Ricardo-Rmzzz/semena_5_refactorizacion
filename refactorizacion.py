def menu_de_opciones():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Ver los resultados guardados hasta ahora')
    print('3: Finalizar')
    return input()

def ingresar_puntuacion_y_comentario():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdigit():  
            point = int(point)
            
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')  
                file_pc.write(f'{ post } \n')       
                file_pc.close()                  
                break
        else:
            print('Por favor, introduzca la puntuación en números')


def ejecutar_programa():
    while True:
        opcion = menu_de_opciones()
        
        if opcion == '1':
            ingresar_puntuacion_y_comentario()
        elif opcion == '2':
            ver_resultados()
        elif opcion == '3':
            print('Finalizando')
            break # Sentencia para finalizar el procesamiento
        else:
            print('Introduzca un número del 1 al 3')


def ver_resultados():
    try:
        file = open('data.txt', 'r')  
        contenido = file.read()       
        file.close()                  
        
        if contenido:                 
            print('Resultados hasta ahora:')
            print(contenido)
        else:
            print('No hay resultados guardados')
    except FileNotFoundError:         
        print('No hay resultados guardados')



ejecutar_programa()