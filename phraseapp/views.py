from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import PhraseForm
from .models import PhraseModel

# Create your views here.

@login_required
def createphrase(request, user_pk):
    phrase_items = PhraseModel.objects.filter(user=request.user.pk)

    if request.method == 'POST':
        form = PhraseForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('phraseapp:createphrase', args=[request.user.pk]))
    else:
        form = PhraseForm()

    content = {
        'user_pk': request.user.pk,
        'phrases': phrase_items,
        'phrase_form': form
    }

    return render(request, 'phraseapp/phrases.html', content)

@login_required
@transaction.atomic
def editphrase(request, user_pk, phrase_pk):
    phrase_instance = get_object_or_404(PhraseModel, pk=phrase_pk)
    form = PhraseForm(request.POST, instance=phrase_instance)

    if request.method == 'POST':
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('phraseapp:createphrase', args=[request.user.pk]))
    else:
        form = PhraseForm(instance=phrase_instance)

    content = {
        'user_pk': request.user.pk,
        'phrase_pk': phrase_pk,
        'phraseedit_form': form
    }

    return render(request, 'phraseapp/phraseedit.html', content)
