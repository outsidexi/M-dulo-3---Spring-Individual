import random

# Lista con los nombres de los futuros usuarios
nombres_usuarios = ["Vet_Doc_1", "Vet_Doc_2", "Vet_Doc_3", "Vet_Doc_4", "Vet_Doc_5", 
                    "Vet_Doc_6", "Vet_Doc_7", "Vet_Doc_8", "Vet_Doc_9", "Vet_Doc_10"]

# Función para crear una contraseña aleatoria
def generar_contraseña():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    longitud = random.randint(8, 12)  # La contraseña tendrá entre 8 y 12 caracteres
    contraseña = ""
    for i in range(longitud):
        contraseña += random.choice(caracteres)
    return contraseña

# Diccionario para almacenar las cuentas de usuario y las contraseñas
cuentas_usuarios = {}

# Ciclo para crear una cuenta y asignarle una contraseña a cada usuario
for nombre in nombres_usuarios:
    contraseña = generar_contraseña()
    cuenta = nombre + "@vetkotcho.com"  # Usamos una dirección de correo electrónico ficticia
    cuentas_usuarios[cuenta] = contraseña
    print(f"Cuenta creada para {nombre}: {cuenta} - Contraseña: {contraseña}")

# Diccionario para almacenar los números de contacto de cada usuario
numeros_contacto = {}

# Ciclo para pedir los números de contacto de cada usuario
while len(numeros_contacto) < len(nombres_usuarios):
    for nombre in nombres_usuarios:
        # Verificar si el número de contacto ya fue ingresado para este usuario
        if nombre not in numeros_contacto:
            numero = input(f"Ingrese el número de contacto para {nombre}: ")
            if numero.isdigit() and len(numero) == 8:
                numeros_contacto[nombre] = numero
            else:
                print("El número debe tener 8 dígitos numéricos.")

# Imprimir las cuentas de usuario y los números de contacto
print("Cuentas de usuario y números de contacto:")
for cuenta, contraseña in cuentas_usuarios.items():
    nombre = cuenta.split("@")[0]
    numero = numeros_contacto[nombre]
    print(f"Cuenta: {cuenta} - Contraseña: {contraseña} - Número de contacto: {numero}")
