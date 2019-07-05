from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from authapp.models import DictUser
from phraseapp.mixins import Mixins_phraseapp, Mixins_phrase_edit
from .forms import PhraseForm
from .models import PhraseModel

# Create your views here.

# @login_required
# def createphrase(request, user_pk):
#     phrase_items = PhraseModel.objects.filter(user=request.user.pk)
#     for_get_form = PhraseForm()
#     for_post_form = PhraseForm(request.POST)
#
#     if request.method == 'POST':
#         form = for_post_form
#         if form.is_valid():
#             #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
#             response = form.save(commit=False)
#             response.user = request.user
#             response.save()
#             return HttpResponseRedirect(reverse('phraseapp:createphrase', args=[request.user.pk]))
#     else:
#         form = for_get_form
#
#     content = {
#         'user_pk': request.user.pk,
#         'phrases': phrase_items,
#         'phrase_form': form
#     }
#
#     return render(request, 'phraseapp/phrases.html', content)

class CreatePhraseView(Mixins_phraseapp, CreateView):
    template = 'phraseapp/phrases.html'
    form_class = PhraseForm

    # pass logged user on to form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePhraseView, self).form_valid(form)

    # pass user_pk on to reverse
    def get_success_url(self):
        user_pk = self.kwargs['user_pk']
        return reverse_lazy('phraseapp:createphrase', kwargs={'user_pk': user_pk})

# @login_required
# @transaction.atomic
# def editphrase(request, user_pk, phrase_pk):
#     phrase_instance = get_object_or_404(PhraseModel, pk=phrase_pk)
#     form = PhraseForm(request.POST, instance=phrase_instance)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             #следующие три строки отвечают за автоматическое добавление юзера в модель, поле юзер на экран не выводится
#             response = form.save(commit=False)
#             response.user = request.user
#             response.save()
#             return HttpResponseRedirect(reverse('phraseapp:createphrase', args=[request.user.pk]))
#     else:
#         form = PhraseForm(instance=phrase_instance)
#
#     content = {
#         'user_pk': request.user.pk,
#         'phrase_pk': phrase_pk,
#         'phraseedit_form': form
#     }
#
#     return render(request, 'phraseapp/phraseedit.html', content)

class EditPhraseView(UpdateView):
    template_name = 'phraseapp/phraseedit.html'
    model = PhraseModel
    form_class = PhraseForm


    pk_url_kwarg = "phrase_pk"

    # def get(self, *args, **kwargs):
    #     user_pk = kwargs.get('user_pk', None)
    #     phrase_pk = kwargs.get('phrase_pk', None)
    #     print(user_pk)
    #     print(phrase_pk)
    #     return super(EditPhraseView, self).get(*args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super(EditPhraseView, self).get_context_data(**kwargs)
    #     context['user_pk'] = user_pk
    #     context['phrase_pk'] = phrase_pk
    #     return context
    #
    # def get_success_url(self):
    #     user_pk = self.kwargs.get('user_pk', None)
    #     phrase_pk = self.kwargs.get('phrase_pk', None)
    #     # user_pk = self.kwargs['user_pk']
    #     # phrase_pk = self.kwargs['phrase_pk']
    #     return reverse_lazy('phraseapp:editphrase', kwargs={'user_pk': user_pk, 'phrase_pk': phrase_pk})


    # def get_context_data(self, **kwargs):
    #     context = super(EditPhraseView, self).get_context_data(**kwargs)
    #     phrase_pk = PhraseModel.objects.get(id=self.kwargs.get('phrase_pk', ''))
    #     context['phrase_pk'] = phrase_pk
    #     return context

    # def get_queryset(self):
    #     user_pk = self.kwargs['user_pk']
    #     phrase_pk = self.kwargs['phrase_pk']
    #     user = get_object_or_404(DictUser, pk=user_pk)
    #     phrase = get_object_or_404(PhraseModel, pk=phrase_pk)


    # slug_url_kwarg = 'thing_id'
    # pk_url_kwarg = 'user_pk'
    # pk_url_kwarg = 'phrase_pk'
    # def get_success_url(self):
    #     user_pk = self.kwargs['user_pk']
    #     phrase_pk = self.kwargs['phrase_pk']
    #     return reverse_lazy('phraseapp:createphrase', kwargs={'user_pk': user_pk, 'phrase_pk': phrase_pk})
    # def get_context_data(self, **kwargs):
    #     context = super(EditPhraseView, self).get_context_data(**kwargs)
    #     # page_alt = Pages.objects.get(id=self.kwargs.get('pk_alt', ''))
    #     context['user_pk'] = PhraseModel.object.get(id=self.kwargs.get('user_pk'))
    #     context['phrase_pk'] = 'phrase_pk'
    #     return context