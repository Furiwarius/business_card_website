import os
import smtplib
from configparser import ConfigParser


def send_bid(massage:str) -> None:
    '''
    Отправка сообщения на почту
    '''
    # Проверка наличия файла ini
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "setting\email.ini")

    if os.path.exists(config_path):
        config = ConfigParser()
        config.read('setting\email.ini')

        # Настройки
        mime = config.get("setting", "mime")
        charset = config.get("setting", "charset")
        server = config.get("setting", "server")
        port = config.get("setting", "port")

        user = config.get("personal data", "email")
        passwd = config.get("personal data", "passwd")
        to = config.get("personal data", "email")
    else:
        return False

    # тема письма
    subject = "Новая заявка"

    # формируем тело письма
    body = "\r\n".join((f"From: {user}", f"To: {to}", 
        f"Subject: {subject}", mime, charset, "", massage))

    try:
        # подключаемся к почтовому сервису
        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(user, passwd)
        # пробуем послать письмо
        smtp.sendmail(user, to, body.encode('utf-8'))
    except smtplib.SMTPException as err:
        print('Что - то пошло не так...')
        raise err
    finally:
        smtp.quit()
