from django import forms
from .models import ExcerptModel

class ExcerptForm(forms.ModelForm):
    class Meta:
            model = ExcerptModel
            fields = ('source', 'excerpt', 'translation')

    def __init__(self, *args, **kwargs):
        super(ExcerptForm, self).__init__(*args, **kwargs)
        self.fields['source'].widget.attrs['placeholder'] = "Excerpt source"
        self.fields['excerpt'].widget.attrs['placeholder'] = "Excerpt"
        self.fields['translation'].widget.attrs['placeholder'] = "Excerpt translation"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'