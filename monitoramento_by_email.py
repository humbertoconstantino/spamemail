
import schedule
import time
import os
from envio_email import Emailer

def send():       #Enviando email:
    mail = Emailer('constantinorpa@gmail.com', 'Hh86604271@')
    lista_contatos = ['humbertoconstantino@outlook.com']
    mail.definir_conteudo('MEU ROBÔ TE ENCONTROU','ConstantinoBOT',lista_contatos,'01010101010101010101010101010101010101010101010101010101010101010100101010101010101010101010101010101010101010101010101010101010101010010101010101010101010101010101010101010101010101010101010101010101001010101010101010101010101010101010101010101010101010101010101010100101010101010101010101010101010101010101010101010101010101010101010010101010101010101010101010101010101010101010101010101010101010101001010101010101010101010101010101010101010101010101010101010101010100101010101010101010101010101010101010101010101010101010101010101010010101010101010101010101010101010101010101010101010101010101010101001010101010101010101010101010101010101010101010')

    mail.enviar_email(1)

schedule.every(2).minutes.do(send)
while True:
    schedule.run_pending()
    time.sleep(1)
#teste teste de novo


