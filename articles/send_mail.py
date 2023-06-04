import smtplib

EMAIL = 'djangodia01@gmail.com'
PASSWORD = 'hiwokujdwfwzoxxf'
def send(obj):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL,PASSWORD)
        
        body = obj['body']

        msg = f'Subject: You have a reaply of comment of csehelp\n\n{body}'
        receiver = obj['receiver']

        print(smtp.sendmail(EMAIL,receiver,msg))
        print(obj)