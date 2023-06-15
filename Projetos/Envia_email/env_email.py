import smtplib

destinatario_email = "bwendel26999@gmail.com"
sender_email = "silentguyband@gmail.com"

message = """
 16:20 hora de f1
 Br marca ess :).
 """

port = 465  
  

with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login("silentguyband@gmail.com", "yiiqhhaedkhrukyn")
    server.sendmail(sender_email, destinatario_email, message)