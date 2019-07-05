from django.conf import settings
from django.db import models


# Create your models here.

#Модель Dictionary это бывшая модель Author; поскольку каждый пользователь будет создавать словари, то первое звено
#цепи в любом случае автор, поэтому словари пользователя это перечень авторов
class Dictionary(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_authors")
    # related_name, чтобы можно было обращаться к объектам модели Dictionary из модели DictUser
    name = models.CharField(verbose_name="Author's name", max_length=64)
    last_name = models.CharField(verbose_name="Author's last name", max_length=64)

    def __str__(self):
        return "{} {}".format(self.name, self.last_name)

class Book(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_books")
    author = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='author_books')
    # related_name, чтобы можно было обращаться к объектам модели Book из модели Dictionary
    title = models.CharField(verbose_name="Book's title", max_length=128)
    image = models.ImageField(upload_to="Book's image", blank=True)

    def __str__(self):
        return "{}".format(self.title)

class Word(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_words")
    author = models.ForeignKey(Dictionary, on_delete=models.CASCADE, related_name='author_words')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='words')
    # related_name, чтобы можно было обращаться к объектам модели Word из модели Book
    word = models.CharField(verbose_name='word', max_length=128)
    translation = models.CharField(verbose_name='translation', max_length=128)
    context = models.TextField(verbose_name='context', blank=True)
    note = models.TextField(verbose_name='note', blank=True)

    def __str__(self):
        return "{}".format(self.word)










# class Word(models.Model):
#     word = models.CharField(verbose_name='word', max_length=128, default=True)
#
#     def __str__(self):
#         return self.word
#
# class Book(models.Model):
#     title = models.CharField(verbose_name="Book's title", max_length=128)
#     members = models.ManyToManyField(Word, through='Membership')
#
#     def __str__(self):
#         return self.title
#
# class Membership(models.Model):
#     word = models.ForeignKey(Word, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
