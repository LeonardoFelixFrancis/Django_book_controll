from django.db import models
from django.conf import settings
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth import get_user_model


# Create your models here.
class BookModel(models.Model):
    book_name = models.CharField(max_length=200)
    rating = models.IntegerField(validators=[MaxLengthValidator(10), MinLengthValidator(1)], null=True,blank=True)
    synopsis = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    start_reading = models.CharField(blank=True, null=True, max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.book_name