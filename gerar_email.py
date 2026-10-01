import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()


def enviar_email(dados):

    remetente = os.getenv("REMETENTE")
    senha = os.getenv("SENHA_DE_APP")
    destinatario = os.getenv("RECEBEDOR")

    mensagem = EmailMessage()

    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = f"Contrato de Adesão - {dados["nome_completo"]}"

    mensagem.set_content(
        "Olá,\n\n"
        "Segue em anexo o contrato de adesão.\n\n"
        "Atenciosamente."
    )

    with open("Contrato.pdf", "rb") as arquivo:
        pdf = arquivo.read()

    mensagem.add_attachment(
        pdf,
        maintype="application",
        subtype="pdf",
        filename="Contrato.pdf"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:

        print("Conectado ao Gmail!")

        servidor.login(remetente, senha)

        print("Login realizado!")

        servidor.send_message(mensagem)

        print("E-mail enviado!")
 

