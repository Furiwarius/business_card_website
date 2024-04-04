from flask import Flask
from app.routes.form_bid import ContactForm
import app.routes.pages as pages


app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
form = ContactForm()
app.register_blueprint(pages.bp)


if __name__ == '__main__':
  # debug true задаем специально для разработки 
  # (в данном случае при обновление/изменение кода приложение 
  # автоматически само обновит данные на сайте)
  app.run(debug=True) 

