import yagmail

def sending_mail(email, password, body_):

        email_client = yagmail.SMTP(email, password)
        
        email_client.send(to="pupbhabua@gmail.com", subject="Message From 'QURE' User", contents=body_)


