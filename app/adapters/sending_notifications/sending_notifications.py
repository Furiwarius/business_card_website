import os
import smtplib
from configparser import ConfigParser
import jinja2


class SenderOfMessages():
    '''
    Отправитель сообщений
    '''
    
    def __init__(self, setting_path:str) -> bool:

        if self.file_availability_check(setting_path):
            self.sender_settings(setting_path)


    def sender_settings(self, setting_path:str) -> None:
        '''
        Чтение настроек из файла ini
        '''

        config = ConfigParser()
        config.read(setting_path)
            # Настройки
        self.mime = config.get("setting", "mime")
        self.charset = config.get("setting", "charset")
        self.server = config.get("setting", "server")
        self.port = config.get("setting", "port")

        self.user = config.get("personal data", "email")
        self.passwd = config.get("personal data", "passwd")
        self.to = config.get("personal data", "email")

        self.subject = config.get("setting letter", "subject")

        self.path_to_letter = config.get("setting letter", "path_to_letter")
        

    def file_availability_check(self, file_path: str) -> bool:
        '''
        Проверка наличия файла ini
        '''


        return os.path.exists(file_path)


    def setting_letter(self, message:str) -> str:
        '''
        Настройка содержания пиьсма
        '''

        body = "\r\n".join((f"From: {self.user}", f"To: {self.to}", 
        f"Subject: {self.subject}", self.mime, self.charset, "", message))

        return body
    

    def send_bid(self, body_message:str) -> None:
        '''
        Отправка сообщения на почту
        '''
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(self.user, self.passwd)
        # пробуем послать письмо
        smtp.sendmail(self.user, self.to, body_message.encode('utf-8'))
        smtp.quit()



    def render_letter(self, username:str, phonnumber:str, email:str) -> str:
        '''
        Вставка данных в шаблон
        '''

        filename = self.path_to_letter

        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        environment = jinja2.Environment()
        template = environment.from_string(template_file_content)
        letter = template.render(username=username,
                                number=phonnumber,
                                email=email)
        
        return letter


    def sending_notifications (self, username:str, phonnumber:str, email:str) -> None:
        '''
        Главный метод-менеджер, принимающий данные и отправляющий их на почту
        '''
        text_letter = self.render_letter(username=username, phonnumber=phonnumber, email=email)
        self.send_bid(self.setting_letter(text_letter))

