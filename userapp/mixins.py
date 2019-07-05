from .models import Dictionary, Book, Word
from phraseapp.models import PhraseModel
from excerptapp.models import ExcerptModel

class Mixins_userapp(object):

    def get_dictionaries(self):
        return Dictionary.objects.all()

    def get_phrases(self):
        return PhraseModel.objects.all()

    def get_context_data(self):
        context = {
            'dicts': self.get_dictionaries(),
            'phrases': self.get_phrases(),
        }
        return context