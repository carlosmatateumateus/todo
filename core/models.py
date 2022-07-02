from django.db import models

class Note(models.Model):

    title = models.CharField(max_length=20)
    finish = models.BooleanField()

    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-update',)