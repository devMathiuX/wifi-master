import subprocess
import os

"""
El codigo tiene muchas partes sin comentar, ya que comparte muchas cosas los metodos
(pedir datos,crea archivos temporales,meter los datos en esos archivos,correr los scripts)

Se definen las variables a utilzar, la de pasos, pasos_temp,y tipo son todas 
las rutas del programa, las otras variables globales son para acceder lo que pusimos
en un metodo desde otro y evitar que tenga que volver a escribir el usuario"""

tipo = "pasos/tipoTarjeta.sh"
paso1 = "pasos/1-modoMonitorON.sh"
paso1_temp = "pasos/temp_1-modoMonitorON.sh"
paso2 = "pasos/2-escanearRedes.sh"
paso2_temp = "pasos/temp_2-escanearRedes.sh"
paso3= "pasos/3-verDispositivos.sh"
paso3_temp = "pasos/temp_3-verDispositivos.sh"
paso4 ="pasos/4-MUERTE.sh"
paso4_temp = "pasos/temp_4-MUERTE.sh"
paso5 = "pasos/5-modoMonitorOFF.sh"
paso5_temp = "pasos/temp_5-modoMonitorOFF.sh"

previo_paso3 = ''
red_mon = None
id = None
#Paso 1
    #Pone la tarjeta de red en modo monitor
def verificacionPaso1():
    if not os.path.isfile(paso1_temp):

        #Verifica el tipo de tarjeta
        resultado_tipo = subprocess.run(['bash', tipo])
        print(resultado_tipo)

        #Solicita el nombre de tarjeta de red en modo normal
        red_normal = input("Ingrese el nombre de la tarjeta de red en modo normal: ")

        #Lee el contenido del script original
        with open(paso1, 'r') as archivo:
            contenido = archivo.read()

        #Reemplaza {TARJETA_NORMAL} con el valor ingresado    
        contenido_modificado = contenido.replace('{TARJETA_NORMAL}', red_normal)

        #Escribe el contenido modificado en un archivo temporal
        with open(paso1_temp, 'w') as archivo_temp:
            archivo_temp.write(contenido_modificado)

        correrPasos(paso1_temp)
            
    else:
        #Ejecuta el script
        correrPasos(paso1_temp)
        
#Paso 2
    #Escanea las redes, necesita del nombre de la tarjeta de red en modo monitor

def verificacionPaso2():
    if not os.path.isfile(paso2_temp): #Si no existe el archivo temporal lo crea

        resultado_tipo = subprocess.run(['bash', tipo])
        print(resultado_tipo)

        global red_mon
        red_mon = input("Ingrese el nombre de la tarjeta de red en modo monitor:")

        with open(paso2, 'r') as archivo:
            contenido = archivo.read()

        # Reemplazar {TARJETA_MONITOR} con el valor ingresado
        contenido_modificado = contenido.replace('{TARJETA_MONITOR}', red_mon)

        with open(paso2_temp, 'w') as archivo_temp:
            archivo_temp.write(contenido_modificado)
            
        correrPasos(paso2_temp)
            
    else: #Si ya existe usa el archivo temporal previo
        resultado_tipo = subprocess.run(['bash', tipo])
        print(resultado_tipo)
        red_mon = input("Ingrese el nombre de la tarjeta de red en modo monitor:")

        correrPasos(paso2_temp)


#Paso 3
    #Entra a la red y ve los dispositivos conectados en ella
def verificacionPaso3():
    global previo_paso3
    global id
    
    if os.path.isfile(paso3_temp): #Se comprueba si ya existe el archivo temporal
        while True:
            previo_paso3 = input("Existe una configuración previa de red. ¿Desea usarla? (s/n): ").strip().lower()
            
            if previo_paso3 == 's':
                correrPasos(paso3_temp)
                break
            elif previo_paso3 == 'n':
                break
            else:
                print("Opción no válida. Por favor, ingrese 's' o 'n'.")
    else:
        previo_paso3 = 'n'

    if previo_paso3 == 'n':
        id = input("Ingrese el BSSID de la red: ")
        canal = input("Ingrese el canal de la red: ")

        with open(paso3, 'r') as archivo:
            contenido = archivo.read()

        contenido_modificado = (
            contenido.replace('{CANAL}', canal)
                     .replace('{BSSID}', id)
                     .replace('{TARJETA_MONITOR}', red_mon)
        )

        with open(paso3_temp, 'w') as archivo_temp:
            archivo_temp.write(contenido_modificado)

        correrPasos(paso3_temp)
            
                
#Paso 4 
    #Utiliza el BSSID(red) y la estacion (dispositivo) para mandarle el ataque
def verificacionPaso4():
    global previo_paso3
    
    if previo_paso3 == 's':
        correrPasos(paso4_temp)
    else:
        estacion = input("Ingrese la station:")
        
        with open(paso4, 'r') as archivo:
            contenido = archivo.read()

                # Reemplazar {BSSID} con el valor ingresado    
        contenido_modificado =(
            contenido.replace('{BSSID}', id)
            .replace('{ESTACION}', estacion)
            .replace('{TARJETA_MONITOR}', red_mon)
        )
        
        with open(paso4_temp, 'w') as archivo_temp:
            archivo_temp.write(contenido_modificado)

        correrPasos(paso4_temp)
        
#Paso 5
    #Volver la tarjeta de red a modo normal
def verificacionPaso5():
    
    if not os.path.isfile(paso5_temp):

        resultado_tipo = subprocess.run(['bash', tipo])
        print(resultado_tipo)

        with open(paso5, 'r') as archivo:
            contenido = archivo.read()

        # Reemplazar {TARJETA_NORMAL} con el valor ingresado    
        contenido_modificado = contenido.replace('{TARJETA_MONITOR}', red_mon)

        with open(paso5_temp, 'w') as archivo_temp:
            archivo_temp.write(contenido_modificado)

        correrPasos(paso5_temp)
            
    else:
        correrPasos(paso5_temp)
            
            
def correrPasos(x_temp): #Metodo para evitar repetir codigo 
        try:
            subprocess.run(['bash', x_temp])
        except FileNotFoundError:
            print(f"No se encontró {x_temp}")
        except Exception as e:
            print(f"Hubo un error al ejecutar el script, error: {e}")          
            
if __name__ == "__main__":
    verificacionPaso1()
    verificacionPaso2()
    verificacionPaso3()
    verificacionPaso4()
    verificacionPaso5()