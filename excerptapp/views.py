from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ExcerptForm
from .models import ExcerptModel

# Create your views here.

@login_required
def createexcerpt(request, user_pk):
    excerpt_items = ExcerptModel.objects.filter(user=request.user.pk)

    if request.method == 'POST':
        form = ExcerptForm(request.POST)
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('excerptapp:createexcerpts', args=[request.user.pk]))
    else:
        form = ExcerptForm()

    content = {
        'user_pk': request.user.pk,
        'excerpts': excerpt_items,
        'excerpt_form': form
    }

    return render(request, 'excerptapp/excerpts.html', content)

@login_required
@transaction.atomic
def editexcerpt(request, user_pk, excerpt_pk):
    excerpt_instance = get_object_or_404(ExcerptModel, pk=excerpt_pk)
    form = ExcerptForm(request.POST, instance=excerpt_instance)

    if request.method == 'POST':
        if form.is_valid():
            #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
            response = form.save(commit=False)
            response.user = request.user
            response.save()
            return HttpResponseRedirect(reverse('excerptapp:createexcerpts', args=[request.user.pk]))
    else:
        form = ExcerptForm(instance=excerpt_instance)

    content = {
        'user_pk': request.user.pk,
        'excerpt_pk': excerpt_pk,
        'excerptedit_form': form
    }

    return render(request, 'excerptapp/excerptedit.html', content)
