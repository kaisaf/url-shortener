from django.db import models
import string
import random

# Create your models here.
class Url(models.Model):
    url = models.URLField(unique=True)
    path = models.CharField(max_length=12, unique=True)
    counter = models.IntegerField(default=0)

    def create_path(self):
        path = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        urls = Url.objects.filter(path=path)
        if len(urls) == 0:
            return path
        else:
            return self.create_path()

    def __str__(self):
        return "{} : {}".format(self.url, self.path)
