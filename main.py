# Brighten a Day Project
# Goal: Create an app that emails positive messages

# Variables, Imports & Constants
import random
import pandas
import smtplib
import os

SEND_FROM = os.environ.get("SEND_FROM")
SEND_TO = os.environ.get("SEND_TO", "").split(",")
PWD = os.environ.get("PWD")

data = pandas.read_csv("quotes.csv")

# Functions
def choose_quote(data_file):
    quote_num = random.randint(0,19)
    quote = data_file["Quotes"][quote_num]
    speaker = data_file["Speaker"][quote_num]
    formatted_quote = f'"{quote}"\n~{speaker}'
    send_email(formatted_quote)
    
def send_email(quote_msg):
    safe_msg = (
        f"From: {SEND_FROM}\n"
        "Subject: Motivational Quote\n"
        "MIME-Version: 1.0\n"
        "Content-Type: text/plain; charset=utf-8\n"
        "\n"
        f"{quote_msg}"
    ).encode("utf-8")
    
    for addr in SEND_TO:
        with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
            connection.starttls()
            connection.login(user=SEND_FROM, password=PWD)
            connection.sendmail(from_addr=SEND_FROM, to_addrs=str(addr), msg=safe_msg)
        
# Executed Code 
choose_quote(data)
