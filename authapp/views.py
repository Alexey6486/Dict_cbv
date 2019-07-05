from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LoginForm, RegistrationForm

# Create your views here.

# def login(request):
#     return render(request, 'authapp/login.html')

# def login(request):
#     if request.method == 'POST': # проверяем, какой пришел запрос, гет или пост
#         pass
#     else: #если не пост, то значит гет, а гет это просто отрисовка страницы, передадим форму на нее
#         form = LoginForm()
#
#         return render(request, 'authapp/login.html', {'login_form': form})



def login(request):
    if request.method == 'POST': # проверяем, какой пришел запрос, гет или пост
        # если пост, то нам нужно получить данные, которые нам отправили
        # создаем форму, в параметрах которой указываем данные, которые нам отправили request.POST (это свойства
        # хранящиеся ввиде словарей)
        form = LoginForm(request.POST)
        username = request.POST['username'] #словарь=значение по ключу username, то, что отправят в инпуте
        password = request.POST['password']
        #все, на данном этапе мы отрисовали форму логин страницы, полей инпута
        #далее пойдет систепа аутентификации

        #у нас теперь есть username и password, которые передаем во встроенную в джанго функцию
        user = auth.authenticate(username=username, password=password)
        #auth проверяет есть ли пользователь в базе и активный ли он
        if user and user.is_active:
            auth.login(request, user) #здесь логиним пользователя
            return HttpResponseRedirect(reverse('userapp:userpage'))
        else: #если пользователя нет или он не активный
            return render(request, 'authapp/login.html', {'login_form': form})
    else:  # если не пост, то значит гет, а гет это просто отрисовка страницы, передадим форму на нее; ИЛИ этот элс
        # в нашем случае будет отрисовать страницу при переходе на нее
        form = LoginForm()
        return render(request, 'authapp/login.html', {'login_form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainpage'))

def registration(request):
    if request.method == 'POST': #здесь аналогично предыдущему контролеру, принимаем данные отправленные методом пост (указывается в form в templates)
        form = RegistrationForm(request.POST) #request.FILE нужен если грузим файлы (у меня ща их нет, нет аватарки), а в form в templates добавляем enctype="multipart/form-data"
        if form.is_valid(): #проверка формы на валидацию и ее сохранение, зачем и как не знаю
            form.save()         #ну к примеру если один из паролей не совпадет, то ответ валидации будет false
            return HttpResponseRedirect(reverse('auth:authlogin'))


    else: #для гет сразу рисуем пустую форму, это вывод ее на экран
        form = RegistrationForm()

    return render(request, 'authapp/registration.html', {'registration_form': form})

