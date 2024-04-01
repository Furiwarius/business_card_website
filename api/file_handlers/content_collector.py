import json

def content_collector_to_dict(**paths) -> dict:
    '''
    Формирование контента

    Принимает словарь из названий файлов, после чего читает
    эти файлы и возвращает данные хранящиеся в них в виде словаря
    '''
    
    # Открываем файл и достаем оттуда данные о названии страницы и ее содержимом
    result = {}
    for name_file, path in paths.items():
      with open(f"content/{path}.json", encoding="utf-8") as f:
        file_content = f.read()
        result[name_file] = json.loads(file_content)

    return result