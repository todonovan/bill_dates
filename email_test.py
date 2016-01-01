import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


bill_message = "This is a test for a bill."

fromaddr = "bill.date.mailer@gmail.com"
toaddr = "terrence.odonovan@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "A MIME test"

body = '''This is a <br>
test e-mail sent using the <b>MIME</b> tool.<br>
We'll see!
'''

msg.attach(MIMEText(body, 'html'))

server = smtplib.SMTP('smtp.gmail.com', 587)
try:
	server.starttls()
	server.login(fromaddr, "billdates")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
except SMTPException:
	print("Error: unable to sent email")
	raw_input("wait...")

raw_input("Waiting...")