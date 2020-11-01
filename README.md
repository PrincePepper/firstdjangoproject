# Первые попытки работы с Django

Сайт с гайдом для первого запуска - [CLICK](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-a-project)  
Сайт по настройке статических файлов(CSS, JS) - [CLICK](https://docs.djangoproject.com/en/3.1/howto/static-files/)

### Необходимые параметры в `settings.py`
- STATIC_URL = '/static/'
- STATIC_ROOT = "main_app/templates"
- STATICFILES_DIRS = [
    BASE_DIR / "main_app/static",]
    
### Необходимые параметры в `views.py`
```
# Create your views here.
def index(request):
    return render(request, 'your_html.html')
```
# Deploy HEROKU

Здесь следует добавить `runtime.txt`, `Procfile`, `requirements.txt`:
- `runtime.txt`
    - здесь указывает версия Python, например `python-3.8.1`
- `Procfile`
    - команду которую должен выполнить heroku.  
    P.S. firstdjangoproject.wsgi вместо `firstdjangoproject` пишется ваше название проекта
- `requirements.txt`
    - библиотеки необходимые для установки
    
##### My contacts:
1. [Telegram](https://tgmsg.ru/princepepper)
2. [Вконтакте](https://vk.com/princepepper)
3. [Instargam](https://www.instagram.com/prince_pepper_official/?hl=ru)
4. <sereda.wk@gmail.com>
