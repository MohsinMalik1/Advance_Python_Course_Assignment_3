import smtplib
import pandas as pd
from datetime import datetime

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = "mohsinmalik13580@gmail.com"
GMAIL_PASSWORD = "bjgi dbxm ecma kqgy"

def send_email(email, subject, motivationalquote):
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
             server.starttls()
             server.login(GMAIL_USER, GMAIL_PASSWORD)
             email_message = f"Subject: {subject}\n\n*** {motivationalquote} ***"
             server.sendmail(GMAIL_USER, email, email_message)

        print(f"Successfully sent email to {email}")

    except Exception as e:
        print(f"Failed to send email to {email} : {e}")

def check_day():
    date = datetime.now()
    day = date.strftime("%A")

    if day == "Sunday" :

        emails = pd.read_csv("emails.csv")

        for index, row in emails.iterrows():
            email = row["email"]

            motivationalquotes = pd.read_csv("motivationalquotes.csv")

            for index, row in motivationalquotes.iterrows():
                motivationalquote = row["motivationalquote"]

                subject = "*** Motivational Quotes ***"
                send_email(email, subject, motivationalquote)

    else :
        print(f"Sorry Today {day} Emails is only send on Monday")

if __name__ == "__main__":
    check_day()
