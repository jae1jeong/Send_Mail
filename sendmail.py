import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
from email.mime.multipart import MIMEMultipart
import config



dt = datetime.datetime.now()
dt = dt.strftime("%Y-%m-%d")


def send_mail(attach=True):
    msg = MIMEMultipart()
    msg['Subject'] = config.Sub
    msg['From'] =  config.From # 보내는 메일 주소
    msg['To'] = config.To  # 받는 메일 주소 

    

    if attach:
        attachments(msg)
    else:
        login(config.Id,config.To,msg)

def attachments(msg):
    msg.attach(MIMEText(config.content,'plain'))
    file_name = config.file_name
    attachment = open(file_name,'rb')

    # Write File name you want to
    f_n = str(dt) + '.xlsx'
    
    # application","octet-stream 타입이란 의미로 이진 파일을 보낼때 사용
    part = MIMEBase("application","vnd.openxmlformats-officedocument.spreadsheetml.sheet")  # 엑셀 파일
    part.set_payload((attachment).read()) 

    # file encoding section
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment', filename= f_n)
    msg.attach(part)
    attachment.close()
    login(config.Id,config.To,config.Pw,msg)



def login(fr,to,pw,msg):

    google_server = smtplib.SMTP_SSL('smtp.gmail.com',465)

    google_server.login(fr,pw)
    google_server.sendmail(fr,to,msg.as_string()) 
    google_server.quit()



