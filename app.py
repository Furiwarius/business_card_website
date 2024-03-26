from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Optional, NumberRange
import json

class ContactForm(Form):
    username = StringField(label="Имя: ", validators=[DataRequired()])
    phonenumber = IntegerField(label="Ваш номер: ", validators=[DataRequired(), NumberRange(11)])
    message = TextAreaField("massage", validators=[Optional()])
    submit = SubmitField("Оставить заявку")


def content_collector_to_dict(**paths) -> dict:
    '''
    Формирование контента

    Создает из текстового файла формата json словарь, 
    который можно будет вставить в шаблон 
    Принимает путь к файлу из которого будет сформирован контент для вставки
    '''
    
    # Открываем файл и достаем оттуда данные о названии страницы и ее содержимом
    result = {}
    for name_file, path in paths.items():
      with open(f"content/{path}.json", encoding="utf-8") as f:
        file_content = f.read()
        result[name_file] = json.loads(file_content)

    return result


app = Flask(__name__)
form = ContactForm()

# Главная страница
@app.route('/')
def home_page():
  filling = content_collector_to_dict(page='home', services_content='services', contacts='contacts')

  return render_template('home.html', filling=filling, form=form)


# Страница с информацией о вакансиях
@app.route('/vacancies_info')
def vacancies_page():
  filling = content_collector_to_dict(page='vacancies_info', contacts='contacts')

  return render_template('detailed_page.html', filling=filling, form=form)


# Страница с информацией об услугах
@app.route('/<path:service_path>')
def service_page(service_path:str):
  filling = content_collector_to_dict(page=f'{service_path}', contacts='contacts')

  return render_template('detailed_page.html', filling=filling, form=form)



# Обработка данных формы
@app.route('/form', methods=['post', 'get'])
def bid():
  form = ContactForm(request.form)
  if request.method == 'POST' and form.validate():
    print(True)
    # ДОРАБОТАТЬ СПОСОБ ХРАНЕНИЯ ДАННЫХ
  filling = content_collector_to_dict(page='home', services_content='services', contacts='contacts')
  return render_template('home.html', filling=filling, form=form)


# Обработка ошибки 404 - страница не найдена
@app.errorhandler(404)
def page_not_found(e):
    filling = content_collector_to_dict(page='page_not_found', contacts='contacts')
    
    return render_template('sample.html', filling=filling), 404


# Обработка ошибки 500 - ошибка сервера
@app.errorhandler(500)
def server_error(e):
    filling = content_collector_to_dict(page='server_error', contacts='contacts')
    
    return render_template('sample.html', filling=filling), 500


# Обработка ошибки 410 - страница удалена
@app.errorhandler(410)
def page_not_found(e):
    filling = content_collector_to_dict(page='page_deleted', contacts='contacts')
    
    return render_template('sample.html', filling=filling), 410


if __name__ == '__main__':
  # debug true задаем специально для разработки 
  # (в данном случае при обновление/изменение кода приложение 
  # автоматически само обновит данные на сайте)
  app.run(debug=True) 

