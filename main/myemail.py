import smtplib


def send_email(receiver, message):
    sender_email = "adityanathtiwari62@gmail.com"
    rec_email = receiver
    passw = "cyfoesllp2020"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, passw)
    server.sendmail(sender_email, rec_email, message)
