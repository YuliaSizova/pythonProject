import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def sendemail():
    fromaddr = "mikkey111@mail.ru"
    toaddr = "mikkey111@mail.ru"
    mypass = "dWDqiYdKQLrr2wgFZaaf"
    reportname = r"C:\Users\omen1\PycharmProjects\pythonProject\HW4\log.txt"

    msg = MIMEMultipart()
    msg["From"] = fromaddr
    msg["To"] = toaddr
    msg["Subject"] = "Отчет по тестам"

    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachement; filename="%s"' %basename(reportname)
        msg.attach(part)

    body = "Отчеты по проведенным тестам"
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


if __name__ == '__main__':
    sendemail()
