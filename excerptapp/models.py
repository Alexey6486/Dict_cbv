from django.db import models
from django.conf import settings

# Create your models here.

class ExcerptModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_excerpt")
    source = models.CharField(verbose_name="Source", max_length=164)
    excerpt = models.CharField(verbose_name='Excerpt', max_length=128)
    translation = models.CharField(verbose_name='Excerpt_translation', max_length=128)

    def __str__(self):
        return "{}".format(self.excerpt)
