from app.adapters.content_collector import content_collector_to_dict
from app.adapters.sending_notifications import SendNotifications
from app.adapters.database.save_notifications import save_notifications
import os
from app.routes.errors import page_not_found
from app.routes.forms import ContactForm
from flask import Blueprint, render_template, request, redirect, url_for
from smtplib import SMTPAuthenticationError
import threading
import app.logger.logger
from app.routes.schemas import UserForm


bp = Blueprint('app', __name__, url_prefix='/', template_folder='app/templates')
form = ContactForm()
sender = SendNotifications()



# Главная страница
@bp.route('/')
def home_page():
  '''
  Главная страница
  '''
  filling:dict = content_collector_to_dict(page='home', services_content='services', contacts='contacts')

  return render_template('home.html', filling=filling, form=form)



# Страница с информацией о вакансиях
@bp.route('/vacancies_info')
def vacancies_page():
  '''
  Страница с информацией о вакансиях
  '''
  filling:dict = content_collector_to_dict(page='vacancies_info', contacts='contacts')

  return render_template('detailed_page.html', filling=filling, form=form)



# Страница с информацией об услугах
@bp.route('/<path:service_path>')
def service_page(service_path:str):
  '''
  Страница с информацией об услугах
  '''
  if os.path.exists(F'app/content/{service_path}.json')==False:

     return page_not_found(e=404, form=form)
  else:
    filling:dict = content_collector_to_dict(page=f'{service_path}', contacts='contacts')

    return render_template('detailed_page.html', filling=filling, form=form)
  


# Обработка данных формы
@bp.route('/form', methods=['post', 'get'])
def bid():
  '''
  Получение данных формы
  '''
  form:UserForm = UserForm(**request.json)
  
  if request.method == 'GET':
    return redirect(url_for('app.home_page'))
  
  elif request.method == 'POST':   
    try:
      threading.Thread(target=sender.sending_notifications, args=(form,)).start()

    except SMTPAuthenticationError:
      save_notifications(form)
  
    return redirect(url_for('app.home_page'))