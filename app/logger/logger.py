import logging
import logging.config
from configparser import ConfigParser
import os

def check_log_file(setting_path:str) -> None:
    '''
    Проверка наличия файла для логов.
    В случае отсутствия, создать файл.
    '''
    file_path = setting_reader(setting_path)
    if os.path.exists(file_path)==False:
        create_log_file(file_path)


def setting_reader(setting_path:str) -> str:
    '''
    Прочитать настройки и вернуть название файла логов
    '''
    config = ConfigParser()
    config.read(setting_path)
    transmitted_attributes = config.get("handler_timedRotatingFileHandler", "args")
    log_file_path = transmitted_attributes[0]

    return log_file_path


def create_log_file(file_path:str) -> None:
    '''
    Создать файл по зданному пути.
    '''
    with open(file_path, "w"):
        pass



log_setting = 'app/logger/log_setting/log.conf'

check_log_file(log_setting)

logging.config.fileConfig(fname=log_setting)

log = logging.getLogger('root')
