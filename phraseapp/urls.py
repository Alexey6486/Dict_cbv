from django.urls import path, include
import phraseapp.views as phraseapp


app_name = 'phrasesurls'
urlpatterns = [
    path('<user_pk>/', phraseapp.createphrase, name='createphrase'),
    path('<user_pk>/<phrase_pk>/', phraseapp.editphrase, name='editphrase')
]