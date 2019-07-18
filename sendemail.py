import email
import mimetypes
import smtplib

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

user = "kasterma@kasterma.net"
pw = "zw3y65k788hecch9"
server = smtplib.SMTP_SSL(host="smtp.fastmail.com", port=465)
server.login(user=user, password=pw)

msg = MIMEMultipart()
msg['To'] = "kasterma@kastermaa.net"
msg['From'] = "kasterma@kasterma.net"
msg['Subject'] = "With file attached"


with open("test_sheet.xlsx", "rb") as f:
    mt = mimetypes.guess_type("test_sheet.xlsx")[0].split("/")
    msg_file = MIMEBase(mt[0], mt[1])
    msg_file.set_payload(f.read())

email.encoders.encode_base64(msg_file)
msg_file.add_header('Content-Disposition', 'attachment', filename="test_sheetttt.xlsx")

msg.attach(msg_file)
server.sendmail("kasterma@kasterma.net", "bart.kastermans@kpn.com", msg.as_string())
