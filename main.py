from datetime import datetime
from horoscope import main_horoscope as mh
from mongodb import main_mongodb as mm

from utils import send_mail

# mh.main_horoscope()
# mm.main_mongodb()

sender_mail_username = ''
sender_mail_password = ''
receiver_mail_username = ''
subject = ''

print(send_mail.send_mail(sender_mail_username, sender_mail_password, 'B-Tool Boot', receiver_mail_username, subject, datetime(1998,8,8)))
