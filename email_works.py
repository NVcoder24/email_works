import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.request
import datetime

sender = None
receiver = None
password = None
logging = False

current_time = datetime.datetime.now()


def log(success=False):
    if logging and success:
        time = f"{current_time.hour}:{current_time.minute}:{current_time.second}"
        date = f"{current_time.day}.{current_time.month}.{current_time.year}"
        print(f"Message on {time} - {date} [From: {sender}, to: {receiver}]")


def send(header, text=None, html=None, url=None):
    if sender is not None:
        if receiver is not None:
            if password is not None:
                global textg
                global htmlg
                global urlg

                textg = text
                htmlg = html
                urlg = url

                message = MIMEMultipart("alternative")

                message["Subject"] = header
                message["From"] = sender
                message["To"] = receiver

                if textg is not None:
                    textg = """{text}""".format(text=textg)
                    part1 = MIMEText(textg, "plain")
                    message.attach(part1)

                if html is not None:
                    textg = ""
                    htmlg = """{html}""".format(html=htmlg)
                    part2 = MIMEText(htmlg, "html")
                    message.attach(part2)

                if url is not None:
                    htmlg = ""
                    textg = ""
                    web = urllib.request.urlopen(urlg)
                    data = web.read()
                    data = str(data)
                    data = data.split("\\n")
                    i = ""
                    for char in data:
                        i = i + char
                    data = i

                    data = data.split("b'")
                    i = ""
                    for char in data:
                        i = i + char
                    data = i

                    part3 = MIMEText(data, "html")
                    message.attach(part3)

                context = ssl.create_default_context()
                try:
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender, password)
                        server.sendmail(sender, receiver, message.as_string())
                        log(True)
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
