from django.db import models
from shortener_app.utils import get_random_alias


# Create your models here.
class URLShortener(models.Model):
    alias = models.CharField(max_length=8, unique=True)  # Alias column with a max length of 8, unique
    original_url = models.URLField()  # URL column for the original URL


ALIAS_LENGTH = 8

class AliasedURL(models.Model):
    alias = models.CharField(primary_key=True,
                             max_length=ALIAS_LENGTH,
                             default=get_random_alias)
    url = models.URLField(blank = False)

    def __str__(self):
        return f"{self.alias} -> {self.url}"
