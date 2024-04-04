from app.adapters.content_collector import content_collector_to_dict
from app.adapters.sending_notifications import sending_notifications
import os
from .errors import page_not_found
from .form_bid import ContactForm, form
from flask import (Blueprint, render_template, request)


bp = Blueprint('app', __name__, url_prefix='/', template_folder='app/templates')


# Главная страница
@bp.route('/')
def home_page():
  filling = content_collector_to_dict(page='home', services_content='services', contacts='contacts')

  return render_template('home.html', filling=filling, form=form)


# Страница с информацией о вакансиях
@bp.route('/vacancies_info')
def vacancies_page():
  filling = content_collector_to_dict(page='vacancies_info', contacts='contacts')

  return render_template('detailed_page.html', filling=filling, form=form)


# Страница с информацией об услугах
@bp.route('/<path:service_path>')
def service_page(service_path:str):
  if os.path.exists(F'app/content/{service_path}.json')==False:
     return page_not_found(e=404, form=form)
  else:
    filling = content_collector_to_dict(page=f'{service_path}', contacts='contacts')

    return render_template('detailed_page.html', filling=filling, form=form)
  

# Обработка данных формы
@bp.route('/form', methods=['post', 'get'])
def bid():
  form = ContactForm(request.form)
  if request.method == 'POST' and form.validate():    
    sending_notifications(username = form.username.data,
                                                number = form.phonenumber.data,
                                                message = form.message.data)

  filling = content_collector_to_dict(page='home', services_content='services', contacts='contacts')
  return render_template('home.html', filling=filling, form=form)