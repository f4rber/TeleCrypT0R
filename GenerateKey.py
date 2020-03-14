from cryptography.fernet import Fernet
from Cryptodome.PublicKey import RSA

logo = r'''
▄ •▄ ▄▄▄ . ▄· ▄▌     ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
█▌▄▌▪▀▄.▀·▐█▪██▌    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
▐▀▀▄·▐▀▀▪▄▐█▌▐█▪    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█.█▌▐█▄▄▌ ▐█▀·.    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
·▀  ▀ ▀▀▀   ▀ •     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀                                                                  
'''

print(logo)

# Fernet
try:
    key = Fernet.generate_key()  # Переменная с ключём

    file = open('key.key', 'wb')  # Открываем файл / Open file
    file.write(key)  # Записываем ключ в файл / Write key to the file
    file.close()  # Закрываем файл / Close the file

    # Если всё прошло успешно пишем что ключ сгенерирован
    # If everything is ok print message
    print("KEY GENERATED SUCCESSFULLY")

except Exception as ex:
    # Если что-то пошло не так пишем сообщение
    # If something goes wrong print message
    print("KEY WASN`T GENERATED SUCCESSFULLY\n" + str(ex))

# AES
try:
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    print("private_key")

    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    print("public_key")
except Exception as ex:
    print("KEY WASN`T GENERATED SUCCESSFULLY\n" + str(ex))

