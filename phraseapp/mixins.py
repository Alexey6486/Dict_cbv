from django.shortcuts import render

from phraseapp.forms import PhraseForm
from phraseapp.models import PhraseModel

class Mixins_phraseapp(object):
    template = None
    form_class = None

    def get(self, request, user_pk):
        context = {
            'form': self.form_class,
            'user_pk': request.user.pk,
            'phrases': PhraseModel.objects.filter(user=request.user.pk),
        }
        print(context)
        return render(request, self.template, context)

class Mixins_phrase_edit(object):
    template = None
    form_class = None
    model = None

    # phrase_instance = get_object_or_404(PhraseModel, pk=phrase_pk)
    # form_class = PhraseForm(request.POST, instance=phrase_instance)

    def post(self, request, user_pk, phrase_pk):
        context = {
            'phrase_pk': phrase_pk,
            'user_pk': request.user.pk,
            'form': self.form_class,
            'model': self.model,
        }
        return render(request, self.template, context)