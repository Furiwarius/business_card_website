from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange
import json

class ContactForm(Form):
    username = StringField(label="Имя: ", validators=[DataRequired()])
    phonenumber = StringField(label="Ваш номер: ", validators=[NumberRange(max=11, min=11), DataRequired()])
    message = TextAreaField("massage", validators=[Optional()])
    submit = SubmitField("Оставить заявку")


def content_collector_to_dict(path:str) -> dict:
    '''
    Формирование контента

    Создает из текстового файла формата json словарь, 
    который можно будет вставить в шаблон 
    Принимает путь к файлу из которого будет сформирован контент для вставки
    '''
    
    # Открываем файл и достаем оттуда данные о названии страницы и ее содержимом
    with open(path, encoding="utf-8") as f:
        file_content = f.read()
        templates = json.loads(file_content)
        
    return templates


app = Flask(__name__)
form = ContactForm()


# Главная страница
@app.route('/')
def home_page():
  page = content_collector_to_dict('content/home.json')
  services_content = content_collector_to_dict('content/services.json')
  contacts = content_collector_to_dict('content/contacts.json')
  vacancies = content_collector_to_dict('content/vacancies.json')
  
  return render_template('home.html', 
                         page=page, 
                         service_content=services_content,
                         contacts=contacts,
                         vacancies=vacancies)

# Главная страница
@app.route('/vacancies_info')
def vacancies_page():
  contacts = content_collector_to_dict('content/contacts.json')
  vacancies_info = content_collector_to_dict('content/vacancies_info.json')
  
  return render_template('vacancies_info.html', 
                         page=vacancies_info,
                         contacts=contacts)


# Страница с информацией о вакансиях
@app.route('/<path:service_path>')
def service_page(service_path:str):
  page = content_collector_to_dict(f"content/{service_path}.json")
  contacts = content_collector_to_dict('content/contacts.json')
  
  return render_template('services_info.html', page=page, contacts=contacts)


'''
# Обработка данных формы
@app.route('/form', methods=['post', 'get'])
def bid():
  message = ''
  if request.method == 'POST':
    name = request.form.get('name')  # запрос к данным формы
    number = request.form.get('number')
    number = request.form.get('number')

    page = content_collector_to_html('content/submitted_bid.json')
    return render_template('sample.html', page_name=page["page_name"], content=page['content'])
  else:
    page = content_collector_to_html('content/contacts.json')
    return render_template('sample.html', page_name=page["page_name"], content=page['content'])
'''

# Обработка ошибки 404 - страница не найдена
@app.errorhandler(404)
def page_not_found(e):
    page = content_collector_to_dict('content/page_not_found.json')
    
    return render_template('sample.html', page=page), 404


# Обработка ошибки 500 - ошибка сервера
@app.errorhandler(500)
def server_error(e):
    page = content_collector_to_dict('content/server_error.json')
    
    return render_template('sample.html', page=page), 500


# Обработка ошибки 410 - страница удалена
@app.errorhandler(410)
def page_not_found(e):
    page = content_collector_to_dict('content/page_deleted.json')
    
    return render_template('sample.html', page=page), 410


if __name__ == '__main__':
  # debug true задаем специально для разработки 
  # (в данном случае при обновление/изменение кода приложение 
  # автоматически само обновит данные на сайте)
  app.run(debug=True) 

