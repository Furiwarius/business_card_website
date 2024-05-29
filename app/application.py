from flask import Flask, Blueprint


class Application():
    '''
    Приложение
    '''
    def __init__(self, template_folder='templates', static_folder='static') -> None:

        # Путь до шаблонов
        self.__template = template_folder
        # Путь до статических файлов (css, js, img)
        self.__static = static_folder

        self.__create_app()
    

    def __create_app(self) -> None:
        '''
        Создать приложение
        '''
        self.__app = Flask(__name__, 
                           template_folder=self.__template, 
                           static_folder=self.__static)


    def add_blueprint(self, blueprint:Blueprint) -> None:
        '''
        Добавить схему к приложению
        '''
        self.__app.register_blueprint(blueprint)


    def run(self, dubug=True) -> None:
        '''
        Запуск приложения
        '''
        
        self.__app.run(debug=dubug) 