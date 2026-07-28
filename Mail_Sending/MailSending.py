############################################################
#   Program : Simple Mail Sending Program
#   Author  : Om Satish Mahale
#   Purpose : To demonstrate how to send mail using Python
#############################################################

import smtplib
from email.message import EmailMessage

############################################################
#
#  Function Name : send_mail
#  Description   : This function is used to send mail using SMTP protocol
#
############################################################
def send_mail(sender,app_password,receiver,subject,body):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender,app_password)

    smtp.send_message(msg)

    smtp.quit

##############################################################
#
#   Function Name : main
#   Description : Driver Code
#
##############################################################

def main():

    sender_email = "r78305863@gmail.com"

    app_password = "dvrh unmj mese ntdy"

    receiver_email = "ommahale1112@gmail.com"

    subject = "Test Mail from Python Script"

    body = "Jay Ganesh," \
    "This is a test mail sent using Marvellous Python" \
    "" \
    "Regards," \
    "Marvellous Infosystems"

    send_mail(sender_email,app_password,receiver_email,subject,body)

    print("Marvellous Mail Sent Successfully")

#########################################################################
#
#   Program Entry Point
#
#########################################################################

if __name__ == "__main__":
    main()