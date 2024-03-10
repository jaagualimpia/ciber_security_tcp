import socket

from AES_Encrypter import AES_Encrypter

def iniciar_servidor(host, puerto, key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind((host, puerto))
        
        servidor.listen()
        print(f"Servidor escuchando en {host}:{puerto}...")
    
        conexion, direccion = servidor.accept()
        
        aes_encrypter = AES_Encrypter()

        with conexion:
            print(f"Conexión establecida desde {direccion[0]}:{direccion[1]}")
            
            datos = conexion.recv(1024)
            decrypted_data = ""

            with open("archivo.txt", "wb") as encrypted_file:
                encrypted_file.write(datos)
                decrypted_data = aes_encrypter.decrypt_aes_cbc(key, datos)
           
            with open("archivo_desencriptado.txt", "w") as decrypted_file:
                decrypted_file.write(decrypted_data)
            
                print(f"Datos recibidos: {decrypted_data}")

HOST = 'localhost'  
PUERTO = 3032  
key = b'\x17\xce\xa2"M,t)\x85\xf7\xc6\x99\x90N2S'

iniciar_servidor(HOST, PUERTO, key)

