import time
import serial

def enviar_comando(ser, comando):
    ser.write((comando + "\n").encode())
    resposta = ser.readline().decode('utf-8').strip()
    print(f"Resposta recebida: {resposta}")

# Pede ao usuário para inserir a porta serial (ex: COM1)
serial_port = input("Digite a porta serial (ex: COM1): ")

# Configuração da porta serial
ser = serial.Serial(serial_port, 9600, timeout=0.5)
time.sleep(2)  # Aguarde para garantir que a porta esteja pronta


# Variável para controlar se a tecla ENTER já foi enviada
tecla_enter_enviada = False

while True:
    # Lê a resposta da porta serial
    resposta = ser.readline().decode('utf-8').strip()
    print(f"Resposta recebida: {resposta}")

    if "Press RETURN to get started!" in resposta:
        ser.write("\r\n".encode())
        print("Tecla ENTER enviada.")
        time.sleep(5)
    elif "Username:" in resposta:
        enviar_comando(ser, "Digito o login")
        time.sleep(3)
    elif "Password:" in resposta:
        enviar_comando(ser, "Digite a senha")
        time.sleep(3)
    elif "%Error opening tftp://255.255.255.255/ap1g2-k9w7-tar.default (connection timed out)ap:" in resposta:
        enviar_comando(ser, "dir flash:")
        time.sleep(3)
    elif "ap:" in resposta:
        enviar_comando(ser, "delete flash:private-multiple-fs")
        time.sleep(3)
    elif 'Are you sure you want to delete "flash:private-multiple-fs" (y/n)?' in resposta:
        enviar_comando(ser, "y")
        time.sleep(3)
    elif 'Are you sure you want to reset the system (y/n)?' in resposta:
        enviar_comando(ser, "y")
        time.sleep(3)
    elif 'File "flash:private-multiple-fs" deleted' in resposta:
        enviar_comando(ser, "reset")
        time.sleep(3)
    elif "AP" in resposta and ">" in resposta:
        enviar_comando(ser, "enable")
        time.sleep(3)
    elif "AP" in resposta and "#" in resposta:
        enviar_comando(ser, "capwap ap controller ip address 'digite aqui seu ip'")
        time.sleep(3)
       
    elif "Press RETURN to get started!" in resposta and not tecla_enter_enviada:
        # Enviar a sequência \r\n para representar a tecla ENTER
        ser.write("\r\n".encode())
        print("Tecla ENTER enviada.")
        tecla_enter_enviada = True  # Marcar que a tecla ENTER foi enviada
        time.sleep(3)
    
