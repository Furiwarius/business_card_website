import json
from datetime import datetime
from app.routes.form_bid import ContactForm



def save_notifications (form:ContactForm) -> None:
        '''
        Метод, который сохраняет отправленные данные в базе данных
        '''