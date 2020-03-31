from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
