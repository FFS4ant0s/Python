import smtplib, ssl

destinatario_email = "silentguyband@gmail.com"
sender_email = "silentguyband@gmail.com"

message = """
 Subject: ASSUNTO

 Ola,

 Este e um exemplo de e-mail enviado com Python."""

port = 465  



with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
    server.login("silentguyband@gmail.com", "yiiqhhaedkhrukyn")
    server.sendmail(sender_email, destinatario_email, message)