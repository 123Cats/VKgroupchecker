import os
import smtplib
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def send_email(addr_to, msg_subj, msg_text):
	addr_from = "an@abo29.ru"
	password = "Ietwqgxfjk12"

	msg = MIMEMultipart()
	msg['From'] = addr_from
	msg['To'] = addr_to
	msg['Subject'] = msg_subj

	body = msg_text
	msg.attach(MIMEText(body, 'plain'))

	server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
	server.login(addr_from, password)
	server.send_message(msg)
	server.quit()




