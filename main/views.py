from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'value': ['Yauheni', '24', 'pip']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
