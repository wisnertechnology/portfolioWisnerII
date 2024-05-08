from django.db import models

# Create your models here.

class Mesaj(models.Model):
    Fullname = models.CharField(max_length=150)
    EmailAddress = models.CharField(max_length=200)
    PhoneNumber = models.CharField(max_length=100)
    Message = models.TextField()

    class Meta:
        verbose_name = "Mesaj"
        verbose_name_plural = "Mesaj yo"

    def __str__(self):
        return self.Fullname
