import json
from datetime import datetime

def save_notifications (username:str, phonnumber:str, email:str) -> None:
        '''
        Метод, который сохраняет отправленные данные в json файл
        '''
        to_json = {"username":username, "phonnumber":phonnumber, "email":email}
        file_name = str(datetime.now()).replace(":", "_")
        file_name = file_name.replace(".", "_")
        with open(f'app/adapters/sending_notifications/saved_messages/massage_{file_name}.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(to_json, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': ')))