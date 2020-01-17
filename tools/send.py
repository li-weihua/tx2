import smtplib
from email.mime.text import MIMEText

def GetIPAddress():
    import os
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    user = os.getenv('USERNAME')
    msg = f'{user}@{socket.gethostname()}: ' + s.getsockname()[0]
    s.close()
    return msg

ip = GetIPAddress()

if __name__ == '__main__':

    from_email = ''
    to_email = from_email
    passwd = ''

    msg = MIMEText(ip)
    msg['Subject'] = 'auto sending ip address'
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        s = smtplib.SMTP_SSL('smtp.qq.com', 465)
        s.login(from_email, passwd)
        s.sendmail(from_email, to_email, msg.as_string())
        s.quit()
        print('sending email success!')
    except Exception as e:
        print(str(e))


