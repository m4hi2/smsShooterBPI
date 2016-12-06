#!/python
''' Yeah, being an Admin of Linux Bangladesh is not the easiest thing to be
'''

from infobip.util.configuration import Configuration
from infobip.clients import send_single_textual_sms
from infobip.api.model.sms.mt.send.textual.SMSTextualRequest import SMSTextualRequest
import xlrd

# Login information
username = ''
password = ''

# XL file information
xl_filename = ''
# sheet_name = ''

# Column number of the column with the phone numbers in a 'Zero Based Index'
column = 3

# infobip configuration
config = Configuration(username, password)
send_sms_client = send_single_textual_sms(config)
request = SMSTextualRequest()

# Change this code to the desired country code.
country_code = '+880'


def getNumber(number):
    '''
    Careless people won't always follow your guideline of +8801XXXXXXXXX, so always prepeare for the worst.
    '''
    if isinstance(number, float):
        string = str(number)
        main_part = string[:10]
        return country_code + main_part
    else:
        return number


def send(number):
    request.to = number
    response = send_sms_client.execute(request)
    print(response)


file = xlrd.open_workbook(xl_filename)
sheet = file.sheet_by_index(0)

i = 1

while True:
    try:
        number = getNumber(sheet.cell(i, column).value)
        request.text = 'Your Message'
        send(number)
        i = i + 1
    except IndexError as e:
        print("sheet is over or some other error occured.")
        print (e)
        break
