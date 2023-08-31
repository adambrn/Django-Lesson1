import datetime
import logging
from django.shortcuts import render
from django.http import HttpResponse

def log_visit(request, page_path):
    logger = logging.getLogger('page_visits')

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown Browser')
    
    log_message = f"{timestamp} - Visited page: {page_path} - User Agent: {user_agent}"
    logger.info(log_message)

def home(request):
    # Логирование данных о посещении страницы
    log_visit(request, request.path)

    html = """
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой первый Django-сайт!</h1>
        <p>Это главная страница сайта.</p>
        <a href="/about/">Перейти на страницу "О себе"</a>
    </body>
    </html>
    """
    return HttpResponse(html)

def about(request):
    # Логирование данных о посещении страницы
    log_visit(request, request.path)

    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Привет! Я создатель этого сайта.</p>
        <a href="/">Вернуться на главную страницу</a>
    </body>
    </html>
    """
    return HttpResponse(html)




