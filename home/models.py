from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=95)
    message = models.TextField(max_length=350)
