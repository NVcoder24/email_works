import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = None
receiver = None
password = None

def send(header, text=None, html=None):
    if sender != None:
        if receiver != None:
            if password != None:
                message = MIMEMultipart("alternative")

                message["Subject"] = header
                message["From"] = sender
                message["To"] = receiver

                if text != None:
                    text = """{text}""".format(text=text)
                    part1 = MIMEText(text, "plain")
                    message.attach(part1)

                if html != None:
                    html = """{html}""".format(html=html)
                    part2 = MIMEText(html, "html")
                    message.attach(part2)

                context = ssl.create_default_context()
                try:
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender, password)
                        server.sendmail(sender, receiver, message.as_string())
                except Exception as e:
                    print(e)
                    print("If you need to solve this problem go issues on github. Or text me on email))")
                    print("https://github.com/NVcoder24/email_works")
            else:
                print("configuration error: password")
        else:
            print("configuration error: reciver email")
    else:
        print("configuration error: sender email")
