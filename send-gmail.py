import json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Corpo da mensagem do email #
msg = MIMEMultipart()
message = "Você recebeu um email da Pycodebr :)"

# Credenciais e assunto do email #
password = "*** SENHA DO EMAIL QUE IRÁ ENVIAR ***"
msg['From'] = "*** EMAIL QUE VAI ENVIAR ***"
msg['To'] = "*** EMAIL QUE VAI RECEBER ***"
msg['Subject'] = "Enviando gmail com Python" # Assunto do email

# Monta conexão e envia o email #
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.starttls()
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()