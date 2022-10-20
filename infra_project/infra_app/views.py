from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Но со второго раза, ведь  нужно прописать ALLOWED_HOSTS +тест')


def second_page(request):
    return HttpResponse('А это вторая страница!')
