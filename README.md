## Telegram CrypT0R bot to crypt your files remotely (made with python 3.8) | Created by F4RB3R
![Made with Python](https://img.shields.io/badge/Made%20with-Python-3572A5.svg)

```
pip install -r requirements.txt

OR

pip install pyTelegramBotAPI
pip install cryptography
pip install pycryptodome or if you use Windows pip install pycryptodomex
```

## Bot Commands:

```
------------------------------
<Welcome to Help>
------------------------------
Bot Commands:
[01] Start
[ /] /start
[02] Help.
[ /] /help
[03] Encrypting one file.
[ /] /encryptone - encrypt only one file
[03] Encrypting all data.
[ /] /encryptall - encripts all files in directory
[04] Shutdown PC.
[ /] /shutdown
[05] Restart PC.
[ /] /restart
------------------------------
<Created by F4RB3R>
------------------------------
'''

## How to use?
```
1) Run GenerateKey.py to generate key.key file

2) Copy the key.key to a USB flash drive, this is necessary so that in the future you can decrypt your files

3) In TeleCrypT0R.py insert the file name for the one you want to encrypt, the bot token and your ID (@userinfobot)

4) In the walk function, insert path to your directory, all files there will be encrypted
```
## Как использовать?
```
1) Запустите GenerateKey.py, чтобы сгенерировать файл key.key

2) Скопируйте key.key на флешку, это нужно для того, чтобы в дальнейшем вы могли расшифровать файл

3) В TeleCrypT0R.py вставьте имя файла для, который вы хотите зашифровать, токен бота и ваш айди (@userinfobot)

4) В функцию walk вставьте путь к своему каталогу, все файлы там будут зашифрованы
```
