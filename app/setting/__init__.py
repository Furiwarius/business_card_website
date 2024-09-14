from app.setting.settings import (SenderNotificationsSetting, SenderErrorssSetting, 
                                  TelegramErrorSenderSetting, TelegramNotificationSenderSetting)


email_setting = SenderNotificationsSetting()
dev_email_setting = SenderErrorssSetting()
tg_setting = TelegramNotificationSenderSetting()
dev_tg_setting = TelegramErrorSenderSetting()
