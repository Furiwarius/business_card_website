from jinja2 import Environment, FileSystemLoader
import json

# Заполнение шаблона
def page_collector(data:dict) -> None:
    '''
    Заполнение шаблона

    Передается только название страницы (page_name)
    и то, что будет отображаться на странице как контент (content).
    В зависимости от того, является ли страница выбранной, меняется и 
    #стиль отображения кнопки.   
    '''
    # Стили кнопок
    button_style = "menu_button"
    selected_style = "selected_button"

    environment = Environment(loader=FileSystemLoader("templates/"))
    # Файл который будет использоваться как шаблон
    template = environment.get_template("sample.html")
    # Имя файла который будет создан при заполнении шаблона
    results_filename = "page.html"

    # Присвоение значений своим тегам в шаблоне
    context = {
        "page_name": data['page_name'],
        "button_style": button_style,
        "selected_button": selected_style,
        "content": data['content']
    }

    # Запись в файл
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(template.render(context))
        print(f"... wrote {results_filename}")

# Сборка контента из файла
def content_collector(path:str) -> dict:
    '''
    Формирование контента

    Создает из текстового файла HTML кусок, 
    который можно будет вставить в шаблон 
    Принимает путь к файлу из которого будет сформирован контент для вставки
    '''

    result_dict = {'page_name':'', 'content':''}
    
    # Открываем файл и достаем оттуда данные о названии страницы и ее содержимом
    with open(path, encoding="utf-8") as f:
        file_content = f.read()
        templates = json.loads(file_content)
    
    # Преобразуем эти данные в словарь с добавлением нужных тегов там, где это необходимо
    for item, data in templates.items():
        if item=="page_name":
            result_dict['page_name'] = data
        elif item=="content":
            for line in data:
                if type(line)==dict:
                    for key in line.keys():
                        if key=="list":
                            result_dict['content']+=list_collector(line["list"])
                        elif key=="phone_number" or key=="email":
                            result_dict['content']+=copy_href_collector(line[key])
                        elif key=="download":
                            result_dict['content']+=f"<p><a href=\"line[key]\" download>Наши реквизиты</a>"
                else:
                    result_dict['content']+=f"<p>{line}</p>"

    return result_dict


# Сборка списков
def list_collector(new_list:list) -> str:
    '''
    Формирование списков

    Создает из полученного списка HTML кусок, 
    который можно будет вставить в шаблон 
    Принимает список, который необходимо преобразовать.
    '''

    result_str = '<ul>'
    for item in new_list:
        result_str += f'<li>{item}</li>'
    result_str += '</ul>'
    
    return result_str


# Сборка ссылок для копирования
def copy_href_collector(value:str) -> str:
    '''
    Формирование ссылок для копирования содержимого

    Создает из полученной строки HTML кусок, 
    который можно будет вставить в шаблон 
    Принимает строку с значением, которое будет вставлено
    в виде ссылки на страницу. При нажатии на ссылку,
    ее содержимое попадет в буфер обмена.
    '''
    result = ""
    result+=f"<script src=\"static\js\copy.js\"></script>" 
    result+=f"<a id=\"{value}\" onclick=\"Copy('{value}')\" class=\"href_copy\">{value}</a>"
    
    return result
