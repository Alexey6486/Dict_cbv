from django.urls import path, include
import userapp.views as userapp
from django.views import View


app_name = 'userdicturls'
urlpatterns = [
    path('', userapp.userpage, name='userpage'),
    path('<user_pk>/dictionaries', userapp.dictionaries, name='dictionaries'),
    # path('<user_pk>/dictionaries', userapp.DictionariesListView.as_view(), name='dictionaries'),
    path('<user_pk>/dictionaries/addauthor', userapp.addauthor, name='addauthor'),
    path('<user_pk>/dictionaries/<author_pk>/authoredit', userapp.authoredit, name='authoredit'),
    path('<user_pk>/dictionaries/<author_pk>/', userapp.books, name='books'),
    path('<user_pk>/dictionaries/<author_pk>/addbook', userapp.addbook, name='addbook'),
    path('<user_pk>/dictionaries/<author_pk>/<book_pk>/bookedit', userapp.bookedit, name='bookedit'),
    path('<user_pk>/dictionaries/<author_pk>/<book_pk>/', userapp.words, name='words'),
    path('<user_pk>/dictionaries/<author_pk>/<book_pk>/addword', userapp.addword, name='addword'),
    path('<user_pk>/dictionaries/<author_pk>/<book_pk>/edit/<word_pk>/', userapp.wordedit, name='wordedit'),
]
