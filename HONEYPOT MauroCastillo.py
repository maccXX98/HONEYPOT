# HONEYPOT

# importacion de librerias
import os
import datetime
import socket

# portada
def portada():
    os.system('cls')
    print("\n\n[+] ¡HONEYPOT Encendido!")
    print("[!] Advertencias activadas si ocurre alguna intrusión.")

# configuracion de honeypot
def configuration():

    os.system('cls')
    print('\a')
    print("\n(Configuracion del HONEYPOT)")

    direction = input('\n\n[-] Ingrese la direccion IP del equipo:')
    try:
        port = int(input('[-] Ingrese el puerto de engaño entre (1-65535):'))
        if (port >= 1 and port <= 65535):
            return (direction, port)
        else:
            print("[x] El número de puerto es incorrecto")
    except ValueError:
        print("[x] El número de puerto ingresado debe ser un entero")

# parametros honeypot
def HONEYPOT(direccionIP, numeroPuerto):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((direccionIP, numeroPuerto))

    server.listen(5)

    alive = True

    while(alive):
        conection, intruso = server.accept()
        mensaje = "\n[+] Intruso detectado desde la direccion{} En {}\n[+] A Hora: {}\n".format(
            str(intruso[0]), intruso[1], datetime.datetime.now().strftime("%c"))
        print(mensaje)

        try:
            conection.close()
        except socket.error:
            pass


# ejecucion honeypot
if __name__ == '__main__':
    try:
        data = configuration()
        if(data != None):
            portada()
            HONEYPOT(data[0], data[1])
        else:
            print("[x] No hay suficiente datos para ejecutar el programa.")
    except KeyboardInterrupt:
        print("Programa HONEYPOT terminado")

# 192.168.1.2
