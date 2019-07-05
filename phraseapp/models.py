from django.db import models
from django.conf import settings

# Create your models here.

class PhraseModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_phrase")
    source = models.CharField(verbose_name="Source", max_length=164)
    phrase = models.CharField(verbose_name='Excerpt', max_length=128)
    translation = models.CharField(verbose_name='Excerpt_translation', max_length=128)
    context = models.TextField(verbose_name='Context', blank=True)

    def __str__(self):
        return "{}".format(self.phrase)