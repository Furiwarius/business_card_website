from app.routes.form_bid import ContactForm
import jinja2
from jinja2.environment import Template
from app.setting import email_setting, tg_setting
from app.clients import EmailSender, TelegramSender


class SendNotifications():
    '''
    Класс отправляющий уведомления о заявках
    '''

    
    email_client:EmailSender = EmailSender(email_setting)
    tg_sender:TelegramSender = TelegramSender(tg_setting)



    def render_letter(self, username:str, phonnumber:str, email:str) -> str:
        '''
        Вставка данных в шаблон
        '''

        filename = email_setting.path_to_letter

        with open(filename, 'r', encoding='utf-8') as template_file:
            template_file_content = template_file.read()
        environment = jinja2.Environment()
        template:Template = environment.from_string(template_file_content)

        letter:str = template.render(username=username,
                                number=phonnumber,
                                email=email)
        
        return letter



    def sending_notifications (self, form:ContactForm) -> None:
        '''
        Главный метод-менеджер, принимающий данные и отправляющий их на почту
        '''
        text_letter = self.render_letter(username=form.username.data, phonnumber=form.phonenumber.data, email=form.email.data)
        self.email_client.send(text_letter)
        self.tg_sender.send(text_letter)
    