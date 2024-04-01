from flask import Flask
from api.forms.bid import ContactForm
import api.routes.pages as pages


app = Flask(__name__)
form = ContactForm()
app.register_blueprint(pages.bp)


if __name__ == '__main__':
  # debug true задаем специально для разработки 
  # (в данном случае при обновление/изменение кода приложение 
  # автоматически само обновит данные на сайте)
  app.run(debug=True) 

