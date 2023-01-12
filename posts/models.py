from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return self.title


class Category(models.Model):
    titel = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title