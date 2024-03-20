from flask import Flask, render_template, request
from template_collector import content_collector
from wtforms import Form, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, NumberRange


app = Flask(__name__)

class ContactForm(Form):
    username = StringField(label="Имя: ", validators=[DataRequired()])
    phonenumber = StringField(label="Ваш номер: ", validators=[NumberRange(max=11, min=11), DataRequired()])
    message = TextAreaField("massage", validators=[Optional()])
    submit = SubmitField("Оставить заявку")

form = ContactForm()


# Главная страница
@app.route('/')
def home_page():
  page = content_collector('content/home.json')
  
  return render_template('sample.html', page_name=page["page_name"], content=page['content'])


# О компании
@app.route('/about_company')
def about_company_page():
  page = content_collector('content/about_company.json')
  
  return render_template('sample.html', page_name=page["page_name"], content=page['content'])


# Услуги
@app.route('/services')
def services_page():
  page = content_collector('content/services.json')
  
  return render_template('sample.html', page_name=page["page_name"], content=page['content'])

# Вакансии
@app.route('/vacancies')
def vacancies_page():
  page = content_collector('content/vacancies.json')

  return render_template('sample.html', page_name=page["page_name"], content=page['content'])

# Контакты
@app.route('/contacts')
def contacts_page():
  page = content_collector('content/contacts.json')

  return render_template('sample.html', page_name=page["page_name"], content=page['content'], form=form)


# Обработка данных формы
@app.route('/form', methods=['post', 'get'])
def bid():
  message = ''
  if request.method == 'POST':
    name = request.form.get('name')  # запрос к данным формы
    number = request.form.get('number')
    number = request.form.get('number')

    page = content_collector('content/submitted_bid.json')
    return render_template('sample.html', page_name=page["page_name"], content=page['content'])
  else:
    page = content_collector('content/contacts.json')
    return render_template('sample.html', page_name=page["page_name"], content=page['content'])


# Обработка ошибки 404 - страница не найдена
@app.errorhandler(404)
def page_not_found(e):
    page = content_collector('content/page_not_found.json')
    
    return render_template('sample.html', page_name=page["page_name"], content=page['content']), 404


# Обработка ошибки 500 - ошибка сервера
@app.errorhandler(500)
def server_error(e):
    page = content_collector('content/server_error.json')
    
    return render_template('sample.html', page_name=page["page_name"], content=page['content']), 500


# Обработка ошибки 410 - страница удалена
@app.errorhandler(410)
def page_not_found(e):
    page = content_collector('content/page_deleted.json')
    
    return render_template('sample.html', page_name=page["page_name"], content=page['content']), 410


if __name__ == '__main__':
  # debug true задаем специально для разработки 
  # (в данном случае при обновление/изменение кода приложение 
  # автоматически само обновит данные на сайте)
  app.run(debug=True) 

