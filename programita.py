import socket
import sys

from AES_Encrypter import AES_Encrypter

def enviar_archivo(host, puerto, archivo, mensaje):
    encrypter = AES_Encrypter()
    key = b'\x17\xce\xa2"M,t)\x85\xf7\xc6\x99\x90N2S'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, puerto))
        message = encrypter.encrypt_aes_cbc(key, mensaje)
        
        sock.sendall(message)
        
        print("Archivo enviado exitosamente.")

HOST = 'host.docker.internal' 
PUERTO = 3032  
ARCHIVO = 'archivo.txt'  

mensaje = "Mensaje por defecto"

if len(str(sys.argv[1])) > 0:
    mensaje = str(sys.argv[1]) 

enviar_archivo(HOST, PUERTO, ARCHIVO, mensaje)
