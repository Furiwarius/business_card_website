import smtplib
from app.setting import SenderNotificationsSetting, SenderErrorssSetting



class EmailSender():
    '''
    Отправитель сообщений
    '''


    def __init__(self, settings: SenderNotificationsSetting|SenderErrorssSetting) -> None:
        self.setting: SenderNotificationsSetting|SenderErrorssSetting = settings



    def setting_letter(self, message:str) -> str:
        '''
        Настройка содержания пиьсма
        '''

        body = "\r\n".join((f"From: {self.setting.EMAIL}", f"To: {self.setting.TO}", 
        f"Subject: {self.setting.subject}", self.setting.mime, self.setting.charset, "", message))

        return body
    


    def send_bid(self, body_message:str) -> None:
        '''
        Отправка сообщения на почту
        '''
        smtp = smtplib.SMTP(self.setting.server, self.setting.port)
        smtp.starttls()
        smtp.ehlo()
        # логинимся на почтовом сервере
        smtp.login(self.setting.EMAIL, self.setting.PASSWORD)
        # пробуем послать письмо
        smtp.sendmail(self.setting.EMAIL, self.setting.TO, body_message.encode('utf-8'))
        smtp.quit()



    def send (self, text:str) -> None:
        '''
        Главный метод, отправляющий сообщения
        '''

        self.send_bid(self.setting_letter(text))

