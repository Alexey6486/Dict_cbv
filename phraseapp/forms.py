from django import forms
from .models import PhraseModel

class PhraseForm(forms.ModelForm):
    class Meta:
            model = PhraseModel
            fields = ('source', 'phrase', 'translation', 'context')

    def __init__(self, *args, **kwargs):
        super(PhraseForm, self).__init__(*args, **kwargs)
        self.fields['source'].widget.attrs['placeholder'] = "Phrase source"
        self.fields['phrase'].widget.attrs['placeholder'] = "Phrase"
        self.fields['translation'].widget.attrs['placeholder'] = "Phrase translation"
        self.fields['context'].widget.attrs['placeholder'] = "Add context"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'