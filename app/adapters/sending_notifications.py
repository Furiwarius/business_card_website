import os
import smtplib
from configparser import ConfigParser
import jinja2


setting_path = "setting\email.ini"


def file_availability_check(file_path: str) -> bool:
    '''
    Проверка наличия файла ini
    '''

    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, file_path)

    return os.path.exists(config_path)


def send_bid(massage:str) -> None:
    '''
    Отправка сообщения на почту
    '''

    if file_availability_check(setting_path):
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
        subject = config.get("setting letter", "subject")
    else:
        return False

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


def render_letter(**values) -> str:
    '''
    Сборка письма по данным формы
    '''

    filename = "letter_sample_with_massage.txt"
    username = values["username"]
    number = values["number"]
    message = values["message"]

    if message==None:
        filename="letter_sample_only_name_and_number.txt"

    with open(f"templates\{filename}", 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    environment = jinja2.Environment()
    template = environment.from_string(template_file_content)
    letter = template.render(username=username,
                             number=number,
                             message=message)
    
    return letter


def sending_notifications (**values) -> None:
    send_bid(render_letter(**values))