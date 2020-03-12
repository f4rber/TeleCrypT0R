from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('key.key', 'wb')  # Открываем файл / Open file
file.write(key)  # Записываем ключ в файл / Write key to the file
file.close()
