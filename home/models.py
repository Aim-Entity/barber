from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=55)
    email = models.EmailField(max_length=95)
    message = models.TextField(max_length=350)

    def __str__(self):
        return f"{self.full_name}: {self.email}"


class Testimonial(models.Model):
    title = models.CharField(max_length=100)
    par = models.CharField(max_length=200)
    face = models.ImageField(upload_to="testimonial_faces")
    name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name
