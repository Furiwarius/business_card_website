from file_handlers.content_collector import content_collector_to_dict
from flask import render_template

# Обработка ошибки 404 - страница не найдена
def page_not_found(e, form):
    filling = content_collector_to_dict(page='page_not_found', contacts='contacts')
    
    return render_template('detailed_page.html', filling=filling, form=form), 404