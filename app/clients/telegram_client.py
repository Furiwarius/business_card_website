from app.setting import TelegramErrorSenderSetting, TelegramNotificationSenderSetting
import asyncio
from aiogram import Bot, Dispatcher



class TelegramSender():
    '''
    Класс для отправки сообщений в телеграмм
    '''


    def __init__(self, setting:TelegramErrorSenderSetting|TelegramNotificationSenderSetting) -> None:
        
        self.setting = setting
        # Объект бота
        self.bot = Bot(token=self.setting.TELEGRAM_API_TOKEN)
        # Диспетчер
        self.dp = Dispatcher()



    async def _send(self, message:str):
        await self.bot.send_message(self.setting.USER_ID, message)
        await self.bot.session.close()



    def send(self, message:str):
        asyncio.run(self._send(message))