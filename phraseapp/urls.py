from django.urls import path, include
import phraseapp.views as phraseapp


app_name = 'phrasesurls'
urlpatterns = [
    path('<user_pk>/', phraseapp.CreatePhraseView.as_view(), name='createphrase'),
    path('<user_pk>/<phrase_pk>/', phraseapp.EditPhraseView.as_view(), name='editphrase')
]