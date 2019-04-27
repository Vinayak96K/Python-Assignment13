import smtplib
import urllib2
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_Connected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib2.URLError as eObj:
        return False

def SendMail(strLog,strMailTo):
    try:
        strfrom ="vinayak.patil0304@gmail.com"
        msg = MIMEMultipart()
        msg['From']=strfrom
        msg['To']=strMailTo
        body = """
        Hello %s,
        Please find attached document which contains log of removed duplicates files
        This is an auto genrated message.
        Thank you,
        Vinayak Mahendra Patil.
        """%(strMailTo)
        Subject='RemoveReportDuplicate log file'
        msg['Subject']=Subject
        msg.attach(MIMEText(body,'plain'))
        attachment = open(strLog,'rb')
        p = MIMEBase('application','octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition','attachment;filename=%s'%(strLog))
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(strfrom,'----------------')         # password removed
        text = msg.as_string()
        s.sendmail(strfrom,strMailTo,text)
        s.quit()
        print('Log file successfully sent through mail!')

    except Exception as eObj:
        print(eObj)