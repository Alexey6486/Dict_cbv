from django import forms
from .models import Dictionary, Book, Word


#данная форма рисуется по модели Dictionary, но пользователя не выводим, оно будет заполняться автоматически
class AuthorCreationForm(forms.ModelForm):
    class Meta:
            model = Dictionary
            fields = ('name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(AuthorCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = "Author's name"
        self.fields['last_name'].widget.attrs['placeholder'] = "Author's surname"

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class BookCreationForm(forms.ModelForm):
    class Meta:
            model = Book
            fields = ('title',)

    def __init__(self, *args, **kwargs):
        super(BookCreationForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = "Book's title"
        self.fields['title'].label = ""

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class WordCreationForm(forms.ModelForm):
    class Meta:
            model = Word
            fields = ('word', 'translation', 'context', 'note')

    def __init__(self, *args, **kwargs):
        super(WordCreationForm, self).__init__(*args, **kwargs)
        self.fields['word'].widget.attrs['placeholder'] = "Word"
        self.fields['translation'].widget.attrs['placeholder'] = "Translation"
        self.fields['context'].widget.attrs['placeholder'] = "Add context"
        self.fields['note'].widget.attrs['placeholder'] = "Add note"

        for field in self.fields:
            self.fields[field].label = ""
            self.fields[field].widget.attrs['class'] = 'form-control'

