from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from userapp.mixins import Mixins_userapp
from .forms import AuthorCreationForm, BookCreationForm, WordCreationForm
from .models import Dictionary, Book, Word
from phraseapp.models import PhraseModel
from excerptapp.models import ExcerptModel
from django.views.generic.list import ListView

# class UserpageListView(ListView): # cbv with two models
#     template_name = 'userapp/userpage.html'
#     context_object_name = 'phrases'
#
#     def get_queryset(self): # on template calls as objects
#         return Dictionary.objects.all()
#
#     def get_context_data(self, **kwargs):
#         context = super(UserpageListView, self).get_context_data(**kwargs) # call get_context_data method via inheritance from class UserpageListView
#         context['phrases'] = PhraseModel.objects.all() # on template calls as phrases
#         return context

class UserpageListView(Mixins_userapp, View):
    def get(self, request, *args, **kwargs):
        mixin_data = super(UserpageListView, self)
        context = mixin_data.get_context_data()
        return render(request, 'userapp/userpage.html', context)

@login_required
def dictionaries(request, user_pk):
    dict_items = Dictionary.objects.filter(user=request.user.pk)
    check = 'контролер авторов считывается'

    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('userapp:dictionaries', args=[request.user.pk]))
    else:
        form = AuthorCreationForm()

    content = {
        'user_pk': request.user.pk,
        'dicts': dict_items,
        'test': check,
        'author_form': form
    }

    return render(request, 'userapp/dictionaries.html', content)

@login_required
@transaction.atomic
def addauthor(request, user_pk):

    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('userapp:dictionaries', args=[request.user.pk]))
    else:
        form = AuthorCreationForm()

    content = {
        'user_pk': request.user.pk,
        'author_form': form
    }

    return render(request, 'userapp/addauthor.html', content)

@login_required
@transaction.atomic
def authoredit(request, user_pk, author_pk):
    dictionary_instance = get_object_or_404(Dictionary, pk=author_pk)
    form = AuthorCreationForm(request.POST, instance=dictionary_instance)

    if request.method == 'POST':
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('userapp:books', args=[request.user.pk, author_pk]))
    else:
        form = AuthorCreationForm(instance=dictionary_instance)

    content = {
        'user_pk': request.user.pk,
        'author_pk': author_pk,
        'authoredit_form': form
    }

    return render(request, 'userapp/authoredit.html', content)

@login_required
@transaction.atomic
def books(request, user_pk, author_pk):
    book_items = Book.objects.filter(author=author_pk, user=request.user.pk)
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    author_name = get_object_or_404(Dictionary, pk=author_pk)
    check = 'контролер книг автора считывается'

    if request.method == 'POST':
        form = BookCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.save()
            return HttpResponseRedirect(reverse('userapp:books', args=[request.user.pk, author_pk]))
    else:
        form = BookCreationForm()

    content = {
        'author_name': author_name,
        'author_pk': author_pk,
        'books': book_items,
        'book_form': form,
        'test': check,
    }

    return render(request, 'userapp/books.html', content)

@login_required
@transaction.atomic
def addbook(request, user_pk, author_pk):
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    author_name = get_object_or_404(Dictionary, pk=author_pk)

    if request.method == 'POST':
        form = BookCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.save()
            return HttpResponseRedirect(reverse('userapp:books', args=[request.user.pk, author_pk]))
    else:
        form = BookCreationForm()

    content = {
        'author_name': author_name,
        'author_pk': author_pk,
        'book_form': form,
    }

    return render(request, 'userapp/addbook.html', content)

@login_required
@transaction.atomic
def bookedit(request, user_pk, author_pk, book_pk):
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    author_name = get_object_or_404(Dictionary, pk=author_pk)

    book_instance = get_object_or_404(Book, pk=book_pk)
    form = BookCreationForm(request.POST, instance=book_instance)

    if request.method == 'POST':
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.save()
            return HttpResponseRedirect(reverse('userapp:words', args=[request.user.pk, author_pk, book_pk]))
    else:
        form = BookCreationForm(instance=book_instance)

    content = {
        'author_name': author_name,
        'author_pk': author_pk,
        'book_pk': book_pk,
        'bookedit_form': form,
    }

    return render(request, 'userapp/bookedit.html', content)

@login_required
def words(request, user_pk, author_pk, book_pk):
    word_items = Word.objects.filter(author=author_pk, user=request.user.pk, book=book_pk)
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)
    check = 'контролер слов книги считывается'

    if request.method == 'POST':
        form = WordCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.book = book_instance
            response.save()
            return HttpResponseRedirect(reverse('userapp:words', args=[request.user.pk, author_pk, book_pk]))
    else:
        form = WordCreationForm()

    content = {
        'author_name': author_instance,
        'book_title': book_instance,
        'author_pk': author_pk,
        'book_pk': book_pk,
        'words': word_items,
        'word_form': form,
        'test': check,
    }

    return render(request, 'userapp/words.html', content)

@login_required
@transaction.atomic
def addword(request, user_pk, author_pk, book_pk):
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)

    if request.method == 'POST':
        form = WordCreationForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.book = book_instance
            response.save()
            return HttpResponseRedirect(reverse('userapp:words', args=[request.user.pk, author_pk, book_pk]))
    else:
        form = WordCreationForm()

    content = {
        'author_name': author_instance,
        'book_title': book_instance,
        'author_pk': author_pk,
        'book_pk': book_pk,
        'word_form': form,
    }

    return render(request, 'userapp/addword.html', content)

@login_required
@transaction.atomic
def wordedit(request, user_pk, author_pk, book_pk, word_pk):

    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)
    word_instance = get_object_or_404(Word, pk=word_pk)
    author_instance = get_object_or_404(Dictionary, pk=author_pk)
    book_instance = get_object_or_404(Book, pk=book_pk)
    form = WordCreationForm(request.POST, instance=word_instance)

    if request.method == 'POST':
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.author = author_instance
            response.book = book_instance
            form.save()
            return HttpResponseRedirect(reverse('userapp:words', args=[request.user.pk, author_pk, book_pk]))
    else:
        form = WordCreationForm(instance=word_instance)

    content = {
        'wordedit_form': form,
        'author_pk': author_pk,
        'book_pk': book_pk,
        'word_pk': word_pk,
        'author_name': author_instance,
        'book_title': book_instance,
    }

    return render(request, 'userapp/wordedit.html', content)

