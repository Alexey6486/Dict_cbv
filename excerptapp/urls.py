from django.urls import path, include
import excerptapp.views as excerptapp


app_name = 'excerptsurls'
urlpatterns = [
    path('<user_pk>/', excerptapp.createexcerpt, name='createexcerpts'),
    path('<user_pk>/<excerpt_pk>/', excerptapp.editexcerpt, name='editexcerpt')
]