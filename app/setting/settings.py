import dotenv
import os
from functools import lru_cache

dotenv.load_dotenv()



class BaseEmailSetting():
    '''
    Класс с общими настройками для email клиента
    '''

    def __init__(self) -> None:
        self.server = 'smtp.yandex.ru'
        self.port = 587
        self.charset = 'Content-Type: text/plain; charset=utf-8'
        self.mime = 'MIME-Version: 1.0'

        self.subject = "New request"
        

        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")



class SenderNotificationsSetting(BaseEmailSetting):
    '''
    Класс с настройками для email клиента по отправке уведомлений о заявках
    '''
    
    @lru_cache
    def __init__(self) -> None:
        super().__init__()
        self.TO = os.getenv("TO")
        self.path_to_letter = r'app\templates\notifications.txt'



class SenderErrorssSetting(BaseEmailSetting):
    '''
    Класс с настройками для email клиента по отправке уведомлений об ошибках
    '''
    
    @lru_cache
    def __init__(self) -> None:
        super().__init__()
        self.TO = os.getenv("DEVELOPER")
        self.path_to_letter = r'app\templates\error_letter.txt'



class BaseTelegramSetting():
    '''
    Класс для настройки клиента по отправке сообщений в telegram
    '''

    def __init__(self) -> None:
        
        # Токен для бота, который будет отправлять логи
        self.TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")



class TelegramErrorSenderSetting(BaseTelegramSetting):
    '''
    Настройки телеграмма для отправки ошибок
    '''

    def __init__(self) -> None:
        super().__init__()

        # id телеграма разработчика, для отправки уведомлений об ошибках
        self.USER_ID = os.getenv("DEVELOPER_TELEGRAM_ID")



class TelegramNotificationSenderSetting(BaseTelegramSetting):
    '''
    Настройки клиента телеграмма для отправки уведомлений
    '''

    def __init__(self) -> None:
        super().__init__()

        # id телеграма владельца, для уведомлений
        self.USER_ID = os.getenv("TELEGRAM_ID")