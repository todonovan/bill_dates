import sys
sys.path.append('C:\\Python34\\Lib\\site-packages')
import os
import openpyxl
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

os.chdir('C:\\Users\\Allison\\Desktop')

####
# ENV-type variables for script
####

SCRIPT_DIR = 'C:\\Users\\terre_000\\Desktop\\bill_dates')
LOG_PATH = SCRIPT_DIR + '\\log.txt'
ERROR_PATH = SCRIPT_DIR + '\\error_log.txt'
TARGET_DAYS = 2
TODAY = datetime.date.today()
TODAY_STR = TODAY.strftime('%m/%d/%Y')
CLIENT = "Allison"
CLIENT_ADDR = "allison.diehl@gmail.com"

####
# Function definitions
####

def read_log(path):
	'''
	Opens the file specified at the path (str) for reading,
	returns the information present (str), and closes file
	'''
	log = open(path, 'r')
	contents = log.read()
	log.close()
	return contents

def write_log(path, mode, contents):
	'''
	Opens the file specified at the path (str) in specified
	mode (str),	writes the contents (str), and closes file
	'''
	log = open(path, mode)
	log.write(contents)
	log.close()
	return

####
# Begin by checking whether script has been run yet today
####

last_run = read_log(LOG_PATH)

if (last_run == TODAY_STR):
	sys.exit()

####
# Use openpyxl to determine in-scope dates
# Store bool value in "is_email_necessary"
####

wb = openpyxl.load_workbook('$$ Budget Tool.xlsx')
dates_sheet = wb.get_sheet_by_name('BILL_DATES')

dates_cols = [dates_sheet.columns[1], dates_sheet.columns[4],
              dates_sheet.columns[7], dates_sheet.columns[10],
              dates_sheet.columns[13], dates_sheet.columns[16],
              dates_sheet.columns[19], dates_sheet.columns[22],
              dates_sheet.columns[25], dates_sheet.columns[28],
              dates_sheet.columns[31]]

####
# Formulate a message if needed
####

####
# Send e-mail if necessary
####
if(is_email_necessary):
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
		write_log(ERROR_PATH, 'r+', "Error sending msg on " + TODAY_STR + "\n")
		server.quit()
		sys.exit()

####
# Clean-up and script exit
####

write_log(LOG_PATH, 'w', TODAY_STR)

sys.exit()