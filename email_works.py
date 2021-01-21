import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class email_works:
    data = {}
    debug = True

    def default(self):
        self.data = {
            "context": ssl.create_default_context(),
            "sender": None,
            "password": None,
            "logged": False
        }

    def __init__(self):
        self.default()

    def debug(self, data=False):
        self.debug = data

    def login(self, data):
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.data["context"]) as server:
                server.login(data["sender"], data["password"])
                self.data["logged"] = True
                self.data["sender"] = data["sender"]
                self.data["password"] = data["password"]
        except Exception as e:
            if self.debug:
                print(f"error was handled in login(): {e}")
            return e

    def logoff(self):
        self.default()

    def send(self, data):
        if self.check_data(self.data) == True:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=self.data["context"]) as server:
                    server.login(self.data["sender"], self.data["password"])
                    server.sendmail(self.data["sender"], data["receiver"], data["message"].as_string())
            except Exception as e:
                if self.debug:
                    print(f"error was handled in send(): {e}")
                return e

    def check_data(self, data):
        if data["password"] != None:
            if data["sender"] != None:
                if data["logged"] != False:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def send_text(self, header, text, receiver):
        if self.check_data(self.data) == True:
            message = MIMEMultipart("alternative")
            message["Subject"] = header
            message["From"] = self.data["sender"]
            message["To"] = receiver
            message.attach(MIMEText(text, "plain"))

            info = {"receiver":receiver,
                    "message":message}

            self.send(info)
        else:
            if self.debug:
                print("you need to login first!")

    def send_html(self, header, html, receiver):
        if self.check_data(self.data) == True:
            message = MIMEMultipart("alternative")
            message["Subject"] = header
            message["From"] = self.data["sender"]
            message["To"] = receiver
            message.attach(MIMEText(html, "html"))

            info = {"receiver": receiver,
                    "message": message}

            self.send(info)
        else:
            if self.debug:
                print("you need to login first!")
