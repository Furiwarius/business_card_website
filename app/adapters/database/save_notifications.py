import json
from datetime import datetime
from app.routes.schemas import UserForm



def save_notifications (form:UserForm) -> None:
        '''
        Метод, который сохраняет отправленные данные в базе данных
        '''