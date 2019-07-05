from django.contrib import admin
from django.urls import path, include
import mainapp.views as mainapp



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('authapp.urls', namespace='auth')), # в теплейтс, адрес ссылки для перехода на страницу логин,
                                                               # будет адрес auth:authlogin, где auth - это здешний
                                                               # namespace, а authlogin - name в authapp/urls
    path('userpage/', include('userapp.urls', namespace='userapp')),
    path('', mainapp.mainpage, name='mainpage'),
    path('userpage/excerpts/', include('excerptapp.urls', namespace='excerptapp')),
    path('userpage/phrases/', include('phraseapp.urls', namespace='phraseapp')),
]
