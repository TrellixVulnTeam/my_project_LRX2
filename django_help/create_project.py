# установка django

# pip install django

# создание нового проекта
# django-admin startproject {name}
# -name название проекта

# запуск отладочного сервера
# python manage.py runserver

# создание нового приложения
# python manage.py startapp bboard

# при создании нового приложения его необходимо зарегестрировать
# settings > INSTALLED_APPS = [... ,
# name_module ]
# -name_apps имя нового приложния

# добавить путь(маршрут) path('какой урл', 'какой контроллер')

# в созданном приложении
# urlpatterns = [
# path('', index)
#    ]

# после создания модели необходимо выполнить миграции
# python manage.py makemigrations name_apps