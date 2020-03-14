from cryptography.fernet import Fernet
logo = r'''
▄ •▄ ▄▄▄ . ▄· ▄▌     ▄▄ • ▄▄▄ . ▐ ▄ ▄▄▄ .▄▄▄   ▄▄▄· ▄▄▄▄▄      ▄▄▄  
█▌▄▌▪▀▄.▀·▐█▪██▌    ▐█ ▀ ▪▀▄.▀·•█▌▐█▀▄.▀·▀▄ █·▐█ ▀█ •██  ▪     ▀▄ █·
▐▀▀▄·▐▀▀▪▄▐█▌▐█▪    ▄█ ▀█▄▐▀▀▪▄▐█▐▐▌▐▀▀▪▄▐▀▀▄ ▄█▀▀█  ▐█.▪ ▄█▀▄ ▐▀▀▄ 
▐█.█▌▐█▄▄▌ ▐█▀·.    ▐█▄▪▐█▐█▄▄▌██▐█▌▐█▄▄▌▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▌.▐▌▐█•█▌
·▀  ▀ ▀▀▀   ▀ •     ·▀▀▀▀  ▀▀▀ ▀▀ █▪ ▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀█▄▀▪.▀  ▀                                                                  
'''

print(logo)

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
